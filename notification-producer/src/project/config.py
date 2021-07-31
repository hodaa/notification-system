# /instance/config.py

import os


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    FLASK_ENV = os.getenv('ENVIRONMENT')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTPLUS_MASK_SWAGGER= False


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@db_producer:3306/swvl'


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
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
