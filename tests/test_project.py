from models.project import Project

def test_project_creation():
    project = Project("CLI Tool", "School project")

    assert project.title == "CLI Tool"
    assert project.description == "School project"