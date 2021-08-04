# /instance/config.py
import os
from dotenv import load_dotenv
env_path = os.getcwd() + '/.env'
load_dotenv(dotenv_path=env_path, verbose=True, override=True)


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    FLASK_ENV = os.getenv('ENVIRONMENT')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTPLUS_MASK_SWAGGER = False
    CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL"),
    CELERY_BACKEND_URL = os.environ.get("CELERY_BACKEND_URL"),
    REDIS_URL = os.environ.get("REDIS_URL"),


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///swvl.db'
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
