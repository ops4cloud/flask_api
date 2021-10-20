import logging
from waitress import serve
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask import Flask, Blueprint
from flask_api import settings
from flask_api.endpoints.restplus import api
from flask_api.databases.mongo import DatabaseMongo
from flask_api.endpoints.auth.auth import ns as auth_namespace
from flask_api.endpoints.users.users import ns as users_namespace
from flask_jwt_extended import JWTManager
from paste.translogger import TransLogger

logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)
app = Flask(__name__)
JWTManager(app)

def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP
    flask_app.config['SECRET_KEY'] = settings.JWT_SECRET_KEY


def initialize_app(flask_app):
    configure_app(flask_app)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    flask_app.register_blueprint(blueprint)
    

def main():
    initialize_app(app)
    serve(TransLogger(app), host='0.0.0.0', port=8888)

if __name__ == "__main__":
    main()
