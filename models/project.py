class Project:
    project_count = 0

    def __init__(self, title, description):
        Project.project_count += 1

        self.id = Project.project_count
        self.title = title
        self.description = description
        self.tasks = []

    def __str__(self):
        return f"Project {self.id}: {self.title}"