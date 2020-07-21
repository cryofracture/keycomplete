import os
import sys
import logging
import psycopg2
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = True
    TESTING = True
    CSRF_ENABLED = True
    SECRET_KEY = os.environ['SECRET_KEY']

class ProductionConfig(Config):
    DEBUG = False
    PRODUCTION = False

class DevelomentConfig(Config):
    DEBUG = True
    TESTING = True
    DEVELOPMENT = True