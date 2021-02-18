import os

from starlette import config
from starlette.config import Config


def app_config():

    if os.path.exists(".env"):
        return Config(".env")
    return Config()

config = app_config()



class Base():
    DEBUG = True

    INCLUDE_SCHEMA=config("INCLUDE_SCHEMA", cast=bool, default=True)
    SECRET_KEY = config("SECRET_KEY",default=os.urandom(32))
    SQLALCHEMY_ECHO = config("SQLALCHEMY_ECHO",cast=bool,default=True)
    SQLALCHEMY_TRACK_MODIFICATIONS = config("SQLALCHEMY_TRACK_MODIFICATIONS",cast=bool,default=False)