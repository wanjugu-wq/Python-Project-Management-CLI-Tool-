class Task:
    task_count = 0

    def __init__(self, title):
        Task.task_count += 1

        self.id = Task.task_count
        self.title = title
        self.status = "Pending"

    def mark_complete(self):
        self.status = "Completed"

    def __str__(self):
        return f"[{self.status}] Task {self.id}: {self.title}"