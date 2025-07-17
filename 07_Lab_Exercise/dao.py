import csv
from datetime import datetime
from task import Task, RecurringTask

class TaskCsvDAO:
    def __init__(self, storage_path):
        self.storage_path = storage_path

    def get_all_tasks(self):
        tasks = []
        try:
            with open(self.storage_path, "r", newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    title = row["title"]
                    date_due = datetime.strptime(row["date_due"], "%Y-%m-%d")
                    completed = row["completed"] == "True"
                    if row["type"] == "RecurringTask":
                        interval = int(row["interval"])
                        task = RecurringTask(title, date_due, interval, completed=completed)
                    else:
                        task = Task(title, date_due, completed)
                    tasks.append(task)
        except FileNotFoundError:
            pass
        return tasks

    def save_all_tasks(self, tasks):
        with open(self.storage_path, "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["title", "type", "date_due", "completed", "interval"])
            writer.writeheader()
            for task in tasks:
                writer.writerow({
                    "title": task.title,
                    "type": type(task).__name__,
                    "date_due": task.date_due.strftime("%Y-%m-%d"),
                    "completed": task.completed,
                    "interval": getattr(task, "interval", "").days if hasattr(task, "interval") else ""
                })