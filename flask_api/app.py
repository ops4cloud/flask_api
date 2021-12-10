import logging
from waitress import serve
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask import Flask, Blueprint
from flask_api.endpoints.restplus import api
from flask_api.endpoints.auth.auth import ns as auth_namespace
from flask_api.endpoints.users.users import ns as users_namespace
from flask_jwt_extended import JWTManager
from paste.translogger import TransLogger

logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)
app = Flask(__name__)
app.config.from_object('config.ConfigProd')
JWTManager(app)

def initialize_app(flask_app):
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    flask_app.register_blueprint(blueprint)
    

def main():
    initialize_app(app)
    serve(TransLogger(app), host='0.0.0.0', port=app.config['WAITRESS_PORT'])

if __name__ == "__main__":
    main()
