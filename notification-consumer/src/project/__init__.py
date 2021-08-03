from flask import Flask
from project.models import db
from project.models import *
from project.config import app_config
from project.documented_endpoints import blueprint as documented_endpoint
from project.routes.users_bp import users_bp
from dotenv import load_dotenv
from celery import Celery
import os

env_path = os.getcwd() + '/.env'
load_dotenv(dotenv_path=env_path, verbose=True, override=True)
config_name = os.getenv('ENVIRONMENT')


def create_app(config_name= 'development'):
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "I am consumer notifications service!"

    app.config.from_object(app_config[config_name])
    db.init_app(app)
    app.register_blueprint(users_bp)
    app.register_blueprint(documented_endpoint)

    return app


def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config["CELERY_BACKEND_URL"],
        broker=app.config["CELERY_BROKER_URL"],
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery
