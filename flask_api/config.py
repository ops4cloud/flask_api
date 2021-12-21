"""Flask configuration."""
from os import environ, path
from dotenv import load_dotenv


load_dotenv(path.join('basedir', '.env'))


class Config:
    """Set Flask config variables."""
    SERVER_NAME = environ.get('SERVER_NAME')
    # Flask settings
    WAITRESS_PORT = environ.get('WAITRESS_PORT', 8888)    
    RESTPLUS_VALIDATE = True
    # PyMongo settings
    MONGO_HOST = environ.get('MONGO_DB_HOST')
    MONGO_PORT = environ.get('MONGO_DB_PORT', 27017)
    MONGO_DB = environ.get('MONGO_DATABASE', 'flaskapi')

class ConfigProd(Config):
    SWAGGER_UI_DOC_EXPANSION = 'list'
    FLASK_DEBUG = False  # Do not use debug mode in production
    JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY')

class ConfigDev(Config):
    SWAGGER_UI_DOC_EXPANSION = 'full'
    JWT_SECRET_KEY = 'replacemeporfavor'