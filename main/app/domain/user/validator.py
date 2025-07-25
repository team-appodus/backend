from kink import inject

from main.app.domain.user.repo import UserRepo


@inject
class UserValidator:
    def __init__(self, user_repo: UserRepo):
        self._user_repo = user_repo
