import pickle
from task import Task

class TaskPickleDAO:
    def __init__(self, storage_path: str) -> None:
        self.storage_path = storage_path

    def get_all_tasks(self) -> list[Task]:
        try:
            with open(self.storage_path, "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            return []

    def save_all_tasks(self, tasks: list[Task]) -> None:
        with open(self.storage_path, "wb") as file:
            pickle.dump(tasks, file)