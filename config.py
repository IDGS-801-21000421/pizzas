import os
from sqlalchemy import create_engine

import urllib

class Config(object):
    SESSION_COOKIE_NAME = False
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin@localhost/pizzas'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    