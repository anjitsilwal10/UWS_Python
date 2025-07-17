from datetime import datetime
from task import Task, RecurringTask

class TaskFactory:
    @staticmethod
    def create_task(title, date_str, interval=None):
        date_due = datetime.strptime(date_str, "%Y-%m-%d")
        if interval:
            return RecurringTask(title, date_due, interval=int(interval))
        return Task(title, date_due)