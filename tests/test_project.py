from models.project import Project

def test_project_creation():
    project = Project("Finish Labs", "Two more labs to go!")

    assert project.title == "Finish Labs"
    assert project.description == "Two more labs to go!"