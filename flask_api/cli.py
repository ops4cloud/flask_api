import getpass
import argparse
from flask_api.databases.mongo import DatabaseMongo

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user', type=str, help='Username of user to create', required=True)
parser.add_argument('-p', '--password', type=str, help='password of user to create')
parser.add_argument('-r', '--roles', nargs='+', help='roles of user to create', required=True)
args = parser.parse_args()

if __name__ == '__main__':
    db = DatabaseMongo()
    if not args.password:
        user_stdin = getpass.getpass(prompt='Password: ', stream=None)
        db.create_users(args.user, args.roles, password=user_stdin)