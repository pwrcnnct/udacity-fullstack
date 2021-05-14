import os
SECRET_KEY = os.urandom(32)
basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = False
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:udacity@localhost:5432/fyyur'
SQLALCHEMY_TRACK_MODIFICATIONS = False