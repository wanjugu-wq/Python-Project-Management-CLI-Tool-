import argparse

from models.user import User

users = [] 

parser = argparse.ArgumentParser(description="Project Management CLI")
subparsers = parser.add_subparsers(dest="command")

add_user = subparsers.add_parser("add-user")
add_user.add_argument("--name", required=True)
add_user.add_argument("--email", required=True)

args = parser.parse_args()

if args.command == "add-user":
    user = User(args.name, args.email)
    users.append(user)

    print(f"User created: {user}")