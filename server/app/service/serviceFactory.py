from .userService import UserService
from .menuService import MenuService


class ServiceFactory:
    @property
    def userService(self):
        return UserService()

    @property
    def menuService(self):
        return MenuService()
