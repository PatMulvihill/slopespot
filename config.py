import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']



class HerokuConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    PORT=5000


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    PORT=8080


class TestingConfig(Config):
    TESTING = True