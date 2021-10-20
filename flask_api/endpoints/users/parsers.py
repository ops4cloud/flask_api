from flask_restplus import reqparse

change_password_arguments = reqparse.RequestParser()
change_password_arguments.add_argument(
    'login', type=str, required=True, help='login')
change_password_arguments.add_argument(
    'old_password', type=str, required=True, help='Old password')
change_password_arguments.add_argument(
    'new_password', type=str, required=True, help='New password')