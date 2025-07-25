from typing import List

import phonenumbers
from appodus_utils import BaseEntity, PageRequest, BaseQueryDto, Object
from pydantic import Field, EmailStr, validator, field_validator
from sqlalchemy import Column, String, JSON


class User(BaseEntity):
    __tablename__ = 'users'
    email = Column(String(60), nullable=False)
    phone = Column(String(25), nullable=True)
    preferred_location = Column(String(30), nullable=False)
    property_types = Column(JSON, nullable=False)
    budget = Column(String(30), nullable=True)
    request_urgency = Column(String(30), nullable=False)


class UserBaseDto(Object):
    email: EmailStr = Field(..., title="Email address", description="Your email address")
    phone: str = Field(..., title="Phone number", description="Your phone number")
    preferred_location: str = Field(..., title="Preferred property location",
                                    description="Your preferred property location")
    property_types: List[str] = Field(..., title="Preferred property types",
                                      description="Your preferred property types")
    budget: str = Field(..., title="Budget Range", description="Your budget range")
    request_urgency: str = Field(..., title="Purchase Timeline", description="Your purchase timeline")

    @field_validator('phone')
    def validate_phone(cls, v):
        try:
            phone_obj = phonenumbers.parse(v, None)
            if not phonenumbers.is_valid_number(phone_obj):
                raise ValueError('Invalid phone number format')
        except phonenumbers.NumberParseException:
            raise ValueError('Invalid phone number format')
        return phonenumbers.format_number(phone_obj, phonenumbers.PhoneNumberFormat.E164)


class CreateUserDto(UserBaseDto):
    pass


class UpdateUserDto(UserBaseDto):
    pass


class SearchUserDto(PageRequest, BaseQueryDto, CreateUserDto):
    pass


class QueryUserDto(BaseQueryDto, CreateUserDto):
    pass
