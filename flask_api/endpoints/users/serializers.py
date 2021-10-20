from flask_restplus import fields
from flask_api.endpoints.restplus import api

change_password = api.model('change_password', {
    'login': fields.String(description='login'),
    'old_password': fields.String(description='old password'),
    'new_password': fields.String(description='new password')
})

change_roles = api.model('change_roles', {
    'login': fields.String(description='login'),
    'roles': fields.List(
        fields.String(example='admin, viewer, owner, reader')
    )
})