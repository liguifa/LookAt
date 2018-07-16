from ..domain import Menu
from ..viewmodels import Menu as vm
from .baseService import BaseService
from sqlalchemy import or_


class MenuService(BaseService):
    def __init__(self):
        from .. import db
        self.db = db

    def get_top_menus(self):
        menus = Menu.query.filter(
            Menu.type == 1
        ).all()
        return vm.convert_to_menu(menus)

    def get_side_menus(self, top_menu_id):
        menus = Menu.query.filter(
            Menu.type == 2,
            or_(
                Menu.parent_id == top_menu_id,
                Menu.parent_id.in_(self.db.session.query(Menu.id).filter(
                    Menu.type == 2,
                    Menu.parent_id == top_menu_id
                ))
            )
        ).all()
        return vm.convert_to_menu(menus)
