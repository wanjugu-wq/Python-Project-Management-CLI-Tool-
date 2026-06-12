import argparse

from models.user import User
from utils.storage import load_data, save_data
from rich.console import Console

console = Console()

users = [] 

parser = argparse.ArgumentParser(description="Project Management CLI")
subparsers = parser.add_subparsers(dest="command")

add_user = subparsers.add_parser("add-user")
list_users = subparsers.add_parser("list-users")

add_user.add_argument("--name", required=True)
add_user.add_argument("--email", required=True)

add_project = subparsers.add_parser("add-project")
add_project.add_argument("--user-id", type=int, required=True)
add_project.add_argument("--title", required=True)
add_project.add_argument("--description", required=True)

list_projects = subparsers.add_parser("list-projects")
list_projects.add_argument("--user-id", type=int, required=True)

add_task = subparsers.add_parser("add-task")
add_task.add_argument("--user-id", type=int, required=True)
add_task.add_argument("--project", required=True)
add_task.add_argument("--title", required=True)

list_tasks = subparsers.add_parser("list-tasks")
list_tasks.add_argument("--user-id", type=int, required=True)
list_tasks.add_argument("--project", required=True)

complete_task = subparsers.add_parser("complete-task")
complete_task.add_argument("--user-id", type=int, required=True)
complete_task.add_argument("--project", required=True)
complete_task.add_argument("--task-id", type=int, required=True)

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
elif args.command == "add-project":
    data = load_data()
    try:
        for user in data["users"]:
            if user["id"] == args.user_id:

                project = {
                "title": args.title,
                "description": args.description,
                "tasks": []
                }

                user["projects"].append(project)

                save_data(data)

                print("Project added successfully.")
                break
    except ValueError as e:
        print(f"Error creating user: {e}")
elif args.command == "list-projects":
    data = load_data()

    for user in data["users"]:
        if user["id"] == args.user_id:

            for project in user["projects"]:
                print(f"Project: {project['title']}")
                print(f"Description: {project['description']}")
                print()
elif args.command == "add-task":
    data = load_data()

    for user in data["users"]:
        if user["id"] == args.user_id:

            for project in user["projects"]:
                if project["title"] == args.project:

                    task = {
                        "id": len(project["tasks"]) + 1,
                        "title": args.title,
                        "status": "Pending"
                    }

                    project["tasks"].append(task)

                    save_data(data)

                    print("Task added successfully.")
                    break
elif args.command == "list-tasks":
    data = load_data()

    for user in data["users"]:
        if user["id"] == args.user_id:

            for project in user["projects"]:
                if project["title"] == args.project:

                    for task in project["tasks"]:
                        status_color = "green" if task["status"] == "Completed" else "yellow"

                        console.print(f"[{status_color}]Task {task['id']} - {task['title']}[/]"
)
elif args.command == "complete-task":
    data = load_data()

    for user in data["users"]:
        if user["id"] == args.user_id:

            for project in user["projects"]:
                if project["title"] == args.project:

                    for task in project["tasks"]:
                        if task["id"] == args.task_id:
                            task["status"] = "Completed"
                            save_data(data)
                            print("Task marked as completed.")
                            break

