from models.task import Task

def test_task_completion():
    task = Task("Coderbyte")

    task.mark_complete()

    assert task.status == "Completed"