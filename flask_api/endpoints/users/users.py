from flask import request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from flask_restplus import Resource
from flask_api.endpoints import users
from flask_api.endpoints.restplus import api
from flask_api.endpoints.users.serializers import change_password, change_roles
from flask_api.databases.mongo import DatabaseMongo
from flask_api.lib.password import PasswordCrypt

ns = api.namespace(
    'Users', description='Users method', security='apikey')


@ns.route('/change_password')
class UsersPasswdRessource(Resource):
    @api.expect(change_password)
    @jwt_required()
    def post(self):
        db_connect = DatabaseMongo()
        user_info = db_connect.check_user_info(request.json['login'])
        admin_info = db_connect.check_user_info(get_jwt_identity())
        passwd = PasswordCrypt()
        passwd_match = passwd.check_encrypted_password(request.json['old_password'], user_info['password'])
        if user_info['login'] == get_jwt_identity() or 'admin' in admin_info['roles']:
            if 'admin' in admin_info['roles'] and passwd_match:
                new_encrypt_pass = passwd.encrypt_password(request.json['new_password'])
                if db_connect.change_password(user_info['login'], new_encrypt_pass['encrypted']):
                    return { 'message': 'password updated'}, 200
            if passwd_match:
                new_encrypt_pass = passwd.encrypt_password(request.json['new_password'])
                if db_connect.change_password(user_info['login'], new_encrypt_pass['encrypted']):
                    return { 'message': 'password updated'}, 200
            else:
                return {'message': 'Password missmatch'}, 401
        return {'message': 'Not permitted'}, 401

@ns.route('/change_roles')
class UsersRolesRessource(Resource):
    @api.expect(change_roles)
    @jwt_required()
    def post(self):
        db_connect = DatabaseMongo()
        current_user = get_jwt_identity()
        info_user = db_connect.check_user_info(current_user)
        if 'admin' in info_user['roles']:
            filter = {
                    'login': request.json['login']
                }
            value = {
                'roles': request.json['roles']
            }
            if db_connect.update_doc(filter, value, 'users'):
                return { 'message': 'User roles updated' }
        return {'message': 'Not permitted'}, 401