from flask import Blueprint
import json
from ..service import ServiceFactory

common_bp = Blueprint(
    'common',
    __name__
)


@common_bp.route('/api/common/top_menus')
def get_top_menus():
    menus = ServiceFactory().menuService.get_top_menus()
    return json.dumps(menus)
