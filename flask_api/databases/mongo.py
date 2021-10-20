import json
import pymongo
from pymongo import MongoClient
from werkzeug import exceptions
from flask_api import settings
from bson.json_util import dumps
from flask_api.lib.password import PasswordCrypt


class DatabaseMongo():
    def __init__(self):
        self.mongo_host = settings.MONGO_HOST
        self.mongo_port = settings.MONGO_PORT
        self.mongo_db = settings.MONGO_DB
        self.client = MongoClient(self.mongo_host, self.mongo_port)
        self.db = self.client[self.mongo_db]

    def create_admin(self):
        if self.check_user_info('admin'):
            self.create_users('admin', ['admin'], password='passwd')
        
    def convert_json(self, bson_load):
        json_str = dumps(bson_load)
        return json.loads(json_str)

    def add_doc(self, document=dict, collection=str):
        try:
            result = self.db[collection].insert_one(document)
        except pymongo.errors.DuplicateKeyError:
            return False
        if result.inserted_id:
            return True

    def update_doc(self, filter=dict, value=dict, collection=str):
        change = {
            "$set": value
        }
        try:
            self.db[collection].update_one(filter, change)
            return True
        except pymongo.errors.PyMongoError:
            return False

    def check_user_info(self, login=str):
        document = {
            "login": login
        }
        query_result = self.db.users.find_one(document)
        if query_result:
            return self.convert_json(query_result)
        return None

    def create_users(self, user=str, roles=list, **kwargs):
        self.db.users.create_index([('login', pymongo.ASCENDING)], unique=True)
        passwdCrypt = PasswordCrypt()
        if 'password' in kwargs:
            password = passwdCrypt.encrypt_password(kwargs.password)
        else:
            password = passwdCrypt.generate_password()
        data = {
            "login": user,
            "password": f"{password.get('encrypted')}",
            "first_connect": False,
            "roles": roles
        }
        try:
            self.db.users.insert_one(data)
            return True
        except pymongo.errors.DuplicateKeyError:
            print(f'User {user} already created !!')
            return False

    def change_password(self, login=str, password=str):
        filter = {
            'login': login
        }
        value = {
            'password': password
        }
        return self.update_doc(filter, value, 'users')