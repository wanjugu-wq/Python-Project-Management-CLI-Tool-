from models.person import Person
from models.project import Project
import json

class User(Person):
    try:
        with open("data/database.json", "r") as file:
            data = json.load(file)
            user_count = len(data.get("users", []))
    except (FileNotFoundError, json.JSONDecodeError):
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