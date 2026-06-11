import argparse

from models.user import User
from utils.storage import load_data, save_data

users = [] 

parser = argparse.ArgumentParser(description="Project Management CLI")
subparsers = parser.add_subparsers(dest="command")

add_user = subparsers.add_parser("add-user")
list_users = subparsers.add_parser("list-users")
add_user.add_argument("--name", required=True)
add_user.add_argument("--email", required=True)

args = parser.parse_args()

if args.command == "add-user":
    data = load_data()

    user = User(args.name, args.email)

    data["users"].append(user.to_dict())

    save_data(data)

    print(f"User created: {user}")

elif args.command == "list-users":
    data = load_data()

    for user in data["users"]:
        print(
            f"User {user['id']}: "
            f"{user['name']} "
            f"({user['email']})"
        )

