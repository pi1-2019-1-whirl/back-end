import os

class BaseConfig:
    """Base config"""
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(BaseConfig):
    """Development config"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class ProdConfig(BaseConfig):
    """Production config"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
