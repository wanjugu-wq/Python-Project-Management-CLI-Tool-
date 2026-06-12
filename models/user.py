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

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise TypeError("Email must be a string")

        if "@" not in value:
            raise ValueError("Email must contain @")

        if "." not in value:
            raise ValueError("Email must contain .")

        self._email = value

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