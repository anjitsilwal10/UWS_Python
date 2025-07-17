import csv
from datetime import datetime
from task import Task, RecurringTask

class TaskCsvDAO:
    def __init__(self, storage_path: str) -> None:
        self.storage_path = storage_path
        self.fieldnames = ["title", "type", "date_due", "completed", "interval", "completed_dates", "date_created"]

    def get_all_tasks(self) -> list[Task]:
        task_list = []
        with open(self.storage_path, "r", newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                title = row["title"]
                task_type = row["type"]
                date_due = datetime.strptime(row["date_due"], "%Y-%m-%d")
                completed = row["completed"].lower() == "true"
                interval = int(row["interval"].split()[0]) if row["interval"] else 0
                date_created = datetime.strptime(row["date_created"], "%Y-%m-%d")
                completed_dates = [datetime.strptime(date.strip(), "%Y-%m-%d") for date in row["completed_dates"].split(",") if date]

                if task_type == "RecurringTask":
                    task = RecurringTask(title, date_due, completed, interval, completed_dates, date_created)
                else:
                    task = Task(title, date_due, completed, date_created)

                task_list.append(task)
        return task_list

    def save_all_tasks(self, tasks: list[Task]) -> None:
        with open(self.storage_path, "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            for task in tasks:
                row = {
                    "title": task.title,
                    "type": "RecurringTask" if isinstance(task, RecurringTask) else "Task",
                    "date_due": task.date_due.strftime("%Y-%m-%d"),
                    "completed": str(task.completed),
                    "date_created": task.date_created.strftime("%Y-%m-%d"),
                    "interval": str(task.interval.days) if isinstance(task, RecurringTask) else "",
                    "completed_dates": ",".join(date.strftime("%Y-%m-%d") for date in task.completed_dates) if isinstance(task, RecurringTask) else ""
                }
                writer.writerow(row)