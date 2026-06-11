from models.person import Person
from models.project import Project

class User(Person):
    user_count = 0

    def __init__(self, name, email):
        super().__init__(name)

        User.user_count += 1
        self.id = User.user_count

        self.email = email
        self.projects = []

    def __str__(self):
        return f"User {self.id}: {self.name} ({self.email})"
    
    def add_project(self, title, description):
        project = Project(title, description)
        self.projects.append(project)
        return project
    
    def to_dict(self):
        return {
        "id": self.id,
        "name": self.name,
        "email": self.email,
        "projects": []
    }