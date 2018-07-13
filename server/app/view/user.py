from flask import Blueprint, request, session
from ..service import ServiceFactory
from ..utils import PasswordHelper
import json

user_bp = Blueprint(
    'user',
    __name__
)


@user_bp.route('/api/user/login/', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    from pprint import pprint
    pprint(vars(request.form))
    user = ServiceFactory().userService.get_user_by_username(username)
    print(password)
    print(PasswordHelper.encrypt(password))
    if user and PasswordHelper.encrypt(password) == user.password:
        session["user"] = {
            "username": user.username,
            "id": user.id}
        return json.dumps({
            "isSuccess": True,
            "message": "login success!"
        })
    return json.dumps({
        "isSuccess": False,
        "message": "用户名或密码错误！"
    })
