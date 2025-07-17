from datetime import datetime, timedelta

class Task:
    def __init__(self, title, date_due, completed=False, date_created=None):
        self.title = title
        self.date_due = date_due
        self.completed = completed
        self.date_created = date_created or datetime.now()

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        return f"{self.title} (created: {self.date_created.date()}, due: {self.date_due.date()}, completed: {self.completed})"


class RecurringTask(Task):
    def __init__(self, title, date_due, interval=7, completed=False, completed_dates=None, date_created=None):
        super().__init__(title, date_due, completed, date_created)
        self.interval = timedelta(days=interval)
        self.completed_dates = completed_dates or []

    def mark_completed(self):
        self.completed_dates.append(datetime.now())
        self.date_due += self.interval

    def __str__(self):
        dates = ", ".join(d.strftime("%Y-%m-%d") for d in self.completed_dates)
        return f"{self.title} [Recurring] (due: {self.date_due.date()}, completed dates: [{dates}])"