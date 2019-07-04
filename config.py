import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    NAME = 'jaljeera'
    VERSION = '0.1'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(basedir, 'jaljeera.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'motham-padithamaanallooo'