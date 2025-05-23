from flask import Flask
from model.Db import db
from config import Config
from controllers.producto import api as producto_api
from controllers.pedido import pedido_api
from controllers.cliente import cliente_api

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(producto_api, url_prefix="/api")
    app.register_blueprint(pedido_api, url_prefix="/api")
    app.register_blueprint(cliente_api, url_prefix="/api")
    return app

app = create_app()
