"""from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from . import database
from flask_login import LoginManager, login_manager

database = SQLAlchemy()


def create_app():
    connector = "mysql+pymysql://{0}:{1}@{2}/{3}".format(database.user, database.password, database.host, database.name)

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = connector
    database.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    from .models import User, Professor

    login_manager = LoginManager()
    login_manager.login_view = 'views.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(str(id))

    return app
    """