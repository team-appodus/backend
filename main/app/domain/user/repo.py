from operator import and_, or_
from typing import Type, Optional, Any, List

from appodus_utils import Page, Utils
from fastapi.encoders import jsonable_encoder
from kink import inject
from sqlalchemy import literal, select, func
from sqlalchemy.ext.asyncio import AsyncSession

from main.app.db.repo import GenericRepo
from main.app.domain.user.models import User, CreateUserDto, UpdateUserDto, SearchUserDto, QueryUserDto, \
    SearchUserAndProfileDto, QueryUserAndProfileDto
from main.app.domain.user.profile.models import Profile, KYCAgent


@inject
class UserRepo(GenericRepo[User, CreateUserDto, UpdateUserDto, QueryUserDto, SearchUserDto]):
    def __init__(self, db: AsyncSession, model: Type[User] = User, query_dto: Type[QueryUserDto] = QueryUserDto):
        super().__init__(db, model, query_dto)
        self.db = db

    async def get_by_email(self, email_address: str) -> Optional[QueryUserDto]:
        stmt = select(self._model).where(
            self._model.deleted.is_(False),
            self._model.email == email_address
        )

        result = await self._session.execute(stmt)
        row = result.scalar_one_or_none()

        converted_user = self._db_utils.build_row_response(row)
        converted_user.password = row.password

        return converted_user

    async def exists_by_email(self, email: str) -> bool:
        stmt = select(literal(True)).where(
            self._model.deleted.is_(False),
            self._model.email == email
        )
        result = await self._session.execute(stmt)
        return result.scalar() is not None


    async def get_user_with_profile_page(self, search_dto: SearchUserAndProfileDto)  -> Page[QueryUserAndProfileDto]:
        page = search_dto.page
        page_size = search_dto.page_size
        offset = page * page_size

        select_stmt = (
            select(
                User.id,
                User.email,
                User.phone,
                User.phone_ext,
                User.firstname,
                User.lastname,
                User.status,
                User.gender,
                User.date_created,
                User.last_active_date,
                Profile.personas,
                Profile.bvn_validated,
                Profile.phone_validated,
                Profile.email_validated,
                Profile.identity_validated,
                Profile.address_validated,
            )
            .join(Profile, User.id == Profile.user_id)
            .where(User.deleted == False)
            # .order_by(User.)
            .offset(offset)
            .limit(page_size)
        )

        select_result = await self._session.execute(select_stmt)
        rows = select_result.all()

        total_stmt = (
            select(func.count())
            .select_from(User)
            .join(Profile, User.id == Profile.user_id)
            .where(User.deleted == False)
        )

        total_result = await self._session.execute(total_stmt)
        total_count = total_result.scalar_one()

        response_rows = self.build_rows_response(rows)
        return self._db_utils.build_page(response_rows, total_count, page, page_size)



    def build_rows_response(self, rows: List[Any]):
        response_rows: List[QueryUserAndProfileDto] = []
        if rows:
            response_rows = [

                QueryUserAndProfileDto(**{
                    "id": Utils.uuid_to_hex(row[0]),
                    "email": row[1],
                    "phone": row[2],
                    "phone_ext": row[3],
                    "firstname": row[4],
                    "lastname": row[5],
                    "status": row[6],
                    "gender": row[7],
                    "date_created": row[8],
                    "last_active_date": row[9],
                    "personas": row[10],
                    "bvn_validated": row[11],
                    "phone_validated": row[12],
                    "email_validated": row[13],
                    "identity_validated": row[14],
                    "address_validated": row[15],
                }, pending_kyc=self.get_pending_kyc(
                    bvn_validated=row[11],
                    phone_validated=row[12],
                    email_validated=row[13],
                    identity_validated=row[14],
                    address_validated=row[15],

                ))
                for row in rows
            ]

        return response_rows

    @staticmethod
    def get_pending_kyc(bvn_validated: bool, phone_validated: bool, email_validated: bool, identity_validated: bool, address_validated: bool):
        kyc_badges = []

        if not email_validated:
            kyc_badges.append(KYCAgent.EMAIL)
        if not phone_validated:
            kyc_badges.append(KYCAgent.PHONE)
        if not bvn_validated:
            kyc_badges.append(KYCAgent.BVN)
        if not address_validated:
            kyc_badges.append(KYCAgent.ADDRESS)
        if not identity_validated:
            kyc_badges.append(KYCAgent.IDENTITY)

        return kyc_badges
