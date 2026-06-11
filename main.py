from models.user import User

user = User("Alex", "alex@gmail.com")

project1 = user.add_project("CLI Tool", "School project")
project2 = user.add_project("AI Bot", "Fun experiment")

task1 = project1.add_task("Build models")
task2 = project1.add_task("Write CLI")
task3 = project1.add_task("Test system")

print(user)

for project in user.projects:
    print("\n", project)

    for task in project.tasks:
        print("  ", task)


task1.mark_complete()

print("\nAfter update: \n")

for project in user.projects:
    print(project)

    for task in project.tasks:
        print("  ", task)