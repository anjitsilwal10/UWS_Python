import datetime
from typing import Any

class Task:
    def __init__(
        self,
        title: str,
        date_due: datetime.datetime,
        completed: bool = False,
        date_created: datetime.datetime = None
    ):
        self.title = title
        self.date_due = date_due
        self.completed = completed
        self.date_created = date_created if date_created else datetime.datetime.now()

    def change_title(self, new_title: str) -> None:
        self.title = new_title

    def change_date_due(self, date_due: datetime.datetime) -> None:
        self.date_due = date_due

    def mark_completed(self) -> None:
        self.completed = True

    def __str__(self) -> str:
        return (
            f"{self.title} (created: {self.date_created.strftime('%Y-%m-%d')}, "
            f"due: {self.date_due.strftime('%Y-%m-%d')}, completed: {self.completed})"
        )


class RecurringTask(Task):
    def __init__(
        self,
        title: str,
        date_due: datetime.datetime,
        completed: bool = False,
        interval: int = 0,
        completed_dates: list[datetime.datetime] = None,
        date_created: datetime.datetime = None
    ):
        super().__init__(title, date_due, completed, date_created)
        self.interval = datetime.timedelta(days=interval)
        self.completed_dates = completed_dates if completed_dates else []

    def _compute_next_due_date(self) -> datetime.datetime:
        return self.date_due + self.interval

    def mark_completed(self) -> None:
        self.completed_dates.append(datetime.datetime.now())
        self.date_due = self._compute_next_due_date()

    def __str__(self) -> str:
        completed_str = ", ".join(date.strftime("%Y-%m-%d") for date in self.completed_dates)
        return (
            f"{self.title} - Recurring (created: {self.date_created.strftime('%Y-%m-%d')}, "
            f"due: {self.date_due.strftime('%Y-%m-%d')}, "
            f"completed_dates: [{completed_str}], interval: {self.interval})"
        )


class TaskFactory:
    @staticmethod
    def create_task(title: str, date: datetime.datetime, **kwargs: Any) -> Task:
        if "interval" in kwargs:
            return RecurringTask(
                title, date,
                kwargs.get("completed", False),
                kwargs["interval"]
            )
        else:
            return Task(
                title, date,
                kwargs.get("completed", False)
            )