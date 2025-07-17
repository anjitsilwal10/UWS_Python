# controllers/TaskManagerController.py
from factory import TaskFactory
from tasklist import TaskList  
from dao import TaskCsvDAO

class TaskManagerController:
    def __init__(self, dao: TaskCsvDAO):
        self.dao = dao
        self.task_list = TaskList()
        tasks = self.dao.get_all_tasks()
        for task in tasks:
            self.task_list.add_task(task)

    def add_task(self, title: str, date_str: str, interval: str = None):
        task = TaskFactory.create_task(title, date_str, interval=interval) if interval else TaskFactory.create_task(title, date_str)
        self.task_list.add_task(task)

    def remove_task(self, ix: int) -> bool:
        return self.task_list.remove_task(ix)

    def save_tasks(self):
        self.dao.save_all_tasks(self.task_list.tasks)

    def view_tasks(self) -> list:
        return self.task_list.tasks

    def check_task_index(self, ix: int) -> bool:
        return 0 <= ix < len(self.task_list.tasks)