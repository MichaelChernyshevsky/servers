from dotenv import load_dotenv
from flask import Flask
import os

from flask_cors import CORS
from flasgger import Swagger
from flask_migrate import Migrate
from api.user.index import user_bp
from api.destination.index import destination_bp
from config.config import get_config

from config.extensions import (
    db,
    bcrypt,
    migrate
)

from model import Contact, ContactCategory, Destination, User, Citizenship, UniversalTip

load_dotenv()

def create_app(config_name=os.getenv("FLASK_ENV", "development"))-> Flask:
    app = Flask(__name__)
    CORS(app, max_age=6000)
    app.config.from_object(get_config(config_name))
    
    init_app(app)
    register_blueprints(app=app)
    register_swagger(app=app)
    return app


def init_app(app):
    db.init_app(app)
    migrate = Migrate(app, db)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

def register_blueprints(app):
    app.register_blueprint(user_bp)
    app.register_blueprint(destination_bp)


def register_swagger(app):
    SWAGGER_TEMPLATE = {
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "\JWT access token"
            }
        }
    }
    swag = Swagger(app, template=SWAGGER_TEMPLATE)
    app.config["SWAGGER"] = {
        "openapi": "3.0.0",
        "title": "Globio api",
        "description": ""
    }
