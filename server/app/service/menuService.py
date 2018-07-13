from ..domain import Menu
from .baseService import BaseService


class MenuService(BaseService):
    def get_top_menus(self):
        menus = Menu.query.filter(
            Menu.type == 1
        ).all()
        return menus
