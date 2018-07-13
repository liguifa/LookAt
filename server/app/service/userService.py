from ..domain import User
from .baseService import BaseService


class UserService(BaseService):
    def __init__(self):
        super().__init__()

    def get_user_by_username(self, username):
        return User.query.filter(
            User.username == username
        ).first()