class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, index):
        if self.check_task_index(index):
            self.tasks.pop(index)

    def get_task(self, index):
        return self.tasks[index]

    def check_task_index(self, index):
        return 0 <= index < len(self.tasks)