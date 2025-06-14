class Tasklist:
    def __init__(self, owner):
        self.owner = owner.upper()
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)