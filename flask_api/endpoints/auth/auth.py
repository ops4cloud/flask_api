import logging
from flask import request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from flask_restplus import Resource
from flask_api.endpoints.restplus import api
from flask_api.endpoints.auth.serializers import auth
from flask_api.endpoints.auth.parsers import user_info_arguments
from flask_api.databases.mongo import DatabaseMongo
from flask_api.lib.password import PasswordCrypt

log = logging.getLogger(__name__)
ns = api.namespace(
    'Auth', description='Authorizations method', security='apikey')


@ns.route('/user_info')
class SearchUserCollection(Resource):
    @api.expect(user_info_arguments)
    @jwt_required()
    def get(self):
        arg = user_info_arguments.parse_args(request)
        search = DatabaseMongo()
        info = search.check_user_info(arg.login)
        if info:
            return info, 200
        return {'message': 'User not found'}, 404


@ns.route('/access_token')
class AccessTokenCollection(Resource):
    @api.expect(auth)
    def post(self):
        passwd = PasswordCrypt()
        search = DatabaseMongo()
        result_query = search.check_user_info(request.json['login'])
        if not result_query:
            return {'message': 'login failed'}, 404
        if passwd.check_encrypted_password(request.json['password'], result_query['password']):
            access_token = create_access_token(identity=request.json['login'], )
            return {"access_token": access_token}, 200
        else:
            return {'message': 'login failed'}, 404
