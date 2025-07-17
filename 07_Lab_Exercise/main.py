# from dao import TaskCsvDAO  # or dao_pickle depending on toggle
from dao import TaskPickleDAO
from controllers.TaskManagerController import TaskManagerController
from ui.CommandLineUI import CommandLineUI

if __name__ == "__main__":
    # dao = TaskCsvDAO("07_Lab_Exercise/tasks.csv")
    dao = TaskPickleDAO("07_Lab_Exercise/task.pkl")
    controller = TaskManagerController(dao)
    ui = CommandLineUI(controller)
    ui.run()