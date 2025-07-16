import csv
# import os
# os.makedirs('Property_Decorator', exist_ok=True)

csv_path = '06_Lab_Exercise/Property_Decorator/tasks.csv'


class Task:
    def __init__(self, title: str, completed: bool = False):
        self.title = title
        self.completed = completed

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"{self.title} [{status}]"


class TaskList:
    def __init__(self):
        self.tasks: list[Task] = []

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    @property
    def uncompleted_tasks(self) -> list[Task]:
        return [task for task in self.tasks if not task.completed]

    def view_tasks(self) -> None:
        print("The following tasks are still to be done:")
        for task in self.uncompleted_tasks:
            ix = self.tasks.index(task)
            print(f"{ix}: {task}")

    def save_to_csv(self, filename: str) -> None:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Title', 'Completed'])
            for task in self.tasks:
                writer.writerow([task.title, task.completed])

    def load_from_csv(self, filename: str) -> None:
        try:
            with open(filename, mode='r') as file:
                reader = csv.DictReader(file)
                self.tasks = [
                    Task(row['Title'], row['Completed'] == 'True')
                    for row in reader
                ]
        except FileNotFoundError:
            print(f"No CSV found at {filename}. Starting fresh.")


if __name__ == '__main__':
    task_list = TaskList()

    
    task_list.load_from_csv(csv_path) # lodadind data tasks from file

    
    task_list.add_task(Task("Finish assignment"))
    task_list.add_task(Task("Study Python OOP", completed=True))
    task_list.add_task(Task("Clean workspace"))

    
    task_list.view_tasks()

    
    task_list.save_to_csv(csv_path) # save the tasks