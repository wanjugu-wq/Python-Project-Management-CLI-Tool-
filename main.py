from models.user import User

user = User("Alex", "alex@gmail.com")

user.add_project("CLI Tool", "School project")
user.add_project("AI Bot", "Fun experiment")

print(user)

for project in user.projects:
    print(project)