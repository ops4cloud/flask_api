# Documentation at https://flask-restplus.readthedocs.io/en/stable/
import logging
from flask_restplus import Api
from flask_jwt_extended.exceptions import NoAuthorizationError

log = logging.getLogger(__name__)

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': "Type in the *'Value'* input box below: **'Bearer &lt;JWT&gt;'**, where JWT is the token"
    }
}

api = Api(version='1.0', title='Portal API',
          description='Backend Flask Api powered API', 
          authorizations=authorizations, 
          security='apikey')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)