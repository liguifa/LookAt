from flask import Blueprint
import json
from ..service import ServiceFactory

common_bp = Blueprint(
    'common',
    __name__
)


@common_bp.route('/api/common/top_menus', methods=['GET'])
def get_top_menus():
    menus = ServiceFactory().menuService.get_top_menus()
    return json.dumps(menus, default=lambda o: o.__dict__, sort_keys=True)


@common_bp.route('/api/common/side_menus/<int:top_menu_id>/', methods=['GET'])
def get_side_menus(top_menu_id):
    menus = ServiceFactory().menuService.get_side_menus(top_menu_id)
    return json.dumps(menus, default=lambda o: o.__dict__, sort_keys=True)
