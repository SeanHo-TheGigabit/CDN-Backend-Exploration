from flask import Flask
from flask_smorest import Api
from app.config import Config
from app import RegisterAppResources


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    api = Api(app)
    api2 = RegisterAppResources.register_resources(api)

    return app
