class CommandLineUI:
    def __init__(self, controller):
        self.controller = controller

    def run(self):
        while True:
            self._print_menu()
            choice = input("Enter choice: ").strip()

            if choice == "1":
                tasks = self.controller.view_tasks()
                for i, task in enumerate(tasks):
                    print(f"{i}. {task}")
            elif choice == "2":
                title = input("Task title: ")
                date_str = input("Due date (YYYY-MM-DD): ")
                interval = input("Interval (days, blank for normal task): ")
                self.controller.add_task(title, date_str, interval or None)
                print("Task added.")
            elif choice == "3":
                try:
                    index = int(input("Enter task index to remove: "))
                    if self.controller.check_task_index(index):
                        self.controller.remove_task(index)
                        print("Task removed.")
                    else:
                        print("Invalid task index.")
                except ValueError:
                    print("Please enter a number.")
            elif choice == "4":
                self.controller.save_tasks()
                print("Tasks saved.")
            elif choice.lower() == "q":
                print("Goodbye!")
                break
            else:
                print("Unknown option, try again.")

    def _print_menu(self):
        print("\nMENU")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Save tasks")
        print("q. Quit")