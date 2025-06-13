class TaskList:
    def __init__(self, owner):
        self.owner = owner
        self.tasks = []

my_task_list = TaskList("John")
print(my_task_list.owner)

someone_else_task_list = TaskList("Jane")
print(someone_else_task_list.owner);