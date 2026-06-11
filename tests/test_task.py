from models.task import Task

def test_task_completion():
    task = Task("Build models")

    task.mark_complete()

    assert task.status == "Completed"