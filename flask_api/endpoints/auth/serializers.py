# Documentation at https://flask-restplus.readthedocs.io/en/stable/

from flask_restplus import fields
from flask_api.endpoints.restplus import api

auth = api.model('Auth', {
    'login': fields.String(description='login'),
    'password': fields.String(description='password')
})