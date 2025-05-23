from flask import Flask
from model.Db import db
from config import Config
from controllers.producto import api as producto_api
from controllers.pedido import pedido_api
from controllers.cliente import cliente_api
import os

def create_app(test_config=None):
    app = Flask(__name__)

    if test_config:
        app.config.from_object(test_config)
    else:
        app.config.from_object(Config)
        
        db_user = os.getenv(Config.DB_USER_ENV)
        db_password = os.getenv(Config.DB_PASSWORD_ENV)
        db_host = os.getenv(Config.DB_HOST_ENV)
        db_name = os.getenv(Config.DB_NAME_ENV)

        if all([db_user, db_password, db_host, db_name]):
            app.config['SQLALCHEMY_DATABASE_URI'] = \
                f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}"
        else:
            app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://user:password@localhost/dbname"

    if app.config.get('TESTING') or app.config.get('SQLALCHEMY_DATABASE_URI'):
        db.init_app(app)
        with app.app_context():
            db.create_all()
    else:
        pass

    app.register_blueprint(producto_api, url_prefix="/api")
    app.register_blueprint(pedido_api, url_prefix="/api")
    app.register_blueprint(cliente_api, url_prefix="/api")
    return app