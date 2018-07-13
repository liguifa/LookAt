from .view import blueprints
from .domain import *  # NOQA
from .main import app
from .main import db
import os

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.getcwd() + '/test.db'
app.secret_key = '1qaz2wssxE'
app.config['SESSION_TYPE'] = 'filesystem'
db.create_all()

for blueprint in blueprints:
    app.register_blueprint(blueprint)