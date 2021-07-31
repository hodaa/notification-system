from flask import Flask
from flask import jsonify
from project.config import app_config
from project.models import db
from project.models import *
import threading
# from project.documented_endpoints import blueprint as documented_endpoint
from project.routes.users_bp import users_bp
# from project.routes.notifications_bp import notifications_bp
from project.models.UserNotification import UserNotification


def create_app(config_name):
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "I am consumer notifications service!"

    app.config.from_object(app_config[config_name])
    db.init_app(app)
    app.register_blueprint(users_bp)
    # app.register_blueprint(notifications_bp)
    # app.register_blueprint(documented_endpoint)

    return app
