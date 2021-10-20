from flask_restplus import reqparse

user_info_arguments = reqparse.RequestParser()
user_info_arguments.add_argument(
    'login', type=str, required=True, help='login')
