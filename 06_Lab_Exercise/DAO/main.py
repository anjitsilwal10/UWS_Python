from task import Task
from datetime import datetime

# Toggle between persistence formats
USE_PICKLE = True

# Import appropriate DAO and define file path
if USE_PICKLE:
    from dao_pickle import TaskPickleDAO
    storage_path = "06_Lab_Exercise/DAO/task.pkl"
    dao = TaskPickleDAO(storage_path)
else:
    from dao import TaskCsvDAO
    storage_path = "06_Lab_Exercise/DAO/tasks.csv"
    dao = TaskCsvDAO(storage_path)

def print_task_list(tasks: list[Task]) -> None:
    if not tasks:
        source = "Pickle" if USE_PICKLE else "CSV"
        print(f"No tasks loaded from {source}.")
    else:
        print("Loaded Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def create_task(title: str, date_str: str) -> Task:
    due_date = datetime.strptime(date_str, "%Y-%m-%d")
    return Task(title, due_date)

if __name__ == "__main__":
    # Loading tasks from file
    tasks = dao.get_all_tasks()
    print_task_list(tasks)

    # Adding multiple tasks with reusable function
    task_data = [
        ("Submit lab report", "2025-08-05"),
        ("Prepare presentation", "2025-08-10"),
        ("Buy groceries", "2025-08-03"),
        ("Play Football", "2025-08-15")
    ]

    for title, date_str in task_data:
        tasks.append(create_task(title, date_str))

    # Saving tasks to the selected format
    dao.save_all_tasks(tasks)
    format_type = "Pickle" if USE_PICKLE else "CSV"
    print(f"\nTasks saved using {format_type} successfully.")