import os
from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    HOST = str(os.environ.get("DB_HOST"))
    DATABASE = str(os.environ.get("DB_NAME"))
    USERNAME = str(os.environ.get("DB_USER"))
    PASSWORD = str(os.environ.get("DB_PASSWORD"))
    PORT = str(os.environ.get("DB_PORT"))

    SQLALCHEMY_DATABASE_URI = 'postgresql://' + USERNAME + ':' + PASSWORD + '@' + HOST + ':' + PORT + '/' \
                              + DATABASE

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    DEBUG = True
