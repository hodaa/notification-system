from flask import Flask
from project.config import app_config
from project.models import db
from project.models import *
from project.documented_endpoints import blueprint as documented_endpoint
from project.routes.users_bp import users_bp
from project.routes.notifications_bp import notifications_bp


def create_app(config_name) -> Flask:
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "I am producer notifications service!"

    app.config.from_object(app_config[config_name])
    db.init_app(app)
    app.register_blueprint(users_bp)
    app.register_blueprint(notifications_bp)
    app.register_blueprint(documented_endpoint)

    return app


