from datetime import datetime, timedelta
from typing import Optional


class Vehicle:
    """Base class for all vehicles."""

    def __init__(self, colour: str, weight: int, max_speed: int, max_range: Optional[int] = None, seats: Optional[int] = None) -> None:
        self.colour = colour
        self.weight = weight
        self.max_speed = max_speed
        self.max_range = max_range
        self.seats = seats

    def move(self, speed: int) -> None:
        print(f"The vehicle is moving at {speed} km/h")


class Car(Vehicle):
    """Car inherits from Vehicle and adds form_factor."""

    def __init__(self, colour: str, weight: int, max_speed: int, form_factor: str, **kwargs) -> None:
        super().__init__(colour, weight, max_speed, **kwargs)
        self.form_factor = form_factor

    def move(self, speed: int) -> None:
        print(f"The car is driving at {speed} km/h")


class Electric(Car):
    """Electric car inherits from Car and adds battery_capacity."""

    def __init__(self, colour: str, weight: int, max_speed: int, form_factor: str, battery_capacity: int, **kwargs) -> None:
        super().__init__(colour, weight, max_speed, form_factor, **kwargs)
        self.battery_capacity = battery_capacity

    def move(self, speed: int) -> None:
        print(f"The electric car is driving at {speed} km/h and has a maximum range of {self.max_range} km")


class Petrol(Car):
    """Petrol car inherits from Car and adds fuel_capacity."""

    def __init__(self, colour: str, weight: int, max_speed: int, form_factor: str, fuel_capacity: int, **kwargs) -> None:
        super().__init__(colour, weight, max_speed, form_factor, **kwargs)
        self.fuel_capacity = fuel_capacity

    def move(self, speed: int) -> None:
        print(f"The petrol car is driving at {speed} km/h and has a maximum range of {self.max_range} km")


class Plane(Vehicle):
    """Plane inherits from Vehicle and adds wingspan."""

    def __init__(self, colour: str, weight: int, max_speed: int, wingspan: int, **kwargs) -> None:
        super().__init__(colour, weight, max_speed, **kwargs)
        self.wingspan = wingspan

    def move(self, speed: int) -> None:
        print(f"The plane is flying at {speed} km/h")


class Propeller(Plane):
    """Propeller plane inherits from Plane and adds propeller_diameter."""

    def __init__(self, colour: str, weight: int, max_speed: int, wingspan: int, propeller_diameter: int, **kwargs) -> None:
        super().__init__(colour, weight, max_speed, wingspan, **kwargs)
        self.propeller_diameter = propeller_diameter

    def move(self, speed: int) -> None:
        print(f"The propeller plane is flying at {speed} km/h")


class Jet(Plane):
    """Jet plane inherits from Plane and adds engine_thrust."""

    def __init__(self, colour: str, weight: int, max_speed: int, wingspan: int, engine_thrust: int, **kwargs) -> None:
        super().__init__(colour, weight, max_speed, wingspan, **kwargs)
        self.engine_thrust = engine_thrust

    def move(self, speed: int) -> None:
        print(f"The jet is flying at {speed} km/h")


class FlyingCar(Car, Plane):
    """FlyingCar inherits from both Car and Plane."""

    def __init__(self, colour: str, weight: int, max_speed: int, form_factor: str, wingspan: int, **kwargs) -> None:
        super().__init__(colour, weight, max_speed, form_factor=form_factor, wingspan=wingspan, **kwargs)

    def move(self, speed: int) -> None:
        print(f"The flying car is driving or flying at {speed} km/h")


class Animal:
    def move(self, speed: int) -> None:
        print(f"The animal is moving at a speed of {speed}")


# ToDoApp Extension: RecurringTask
        
class Task:
    def __init__(self, title: str, date_due: datetime) -> None:
        self.title = title
        self.date_created = datetime.now()
        self.date_due = date_due
        self.completed = False

    def mark_completed(self) -> None:
        self.completed = True

    def __str__(self) -> str:
        return f"{self.title} (Due: {self.date_due.date()}, Completed: {self.completed})"


class RecurringTask(Task):
    def __init__(self, title: str, date_due: datetime, interval: timedelta) -> None:
        super().__init__(title, date_due)
        self.interval = interval
        self.completed_dates: list[datetime] = []

    def _compute_next_due_date(self) -> datetime:
        return self.date_due + self.interval

    def mark_completed(self) -> None:
        self.completed_dates.append(datetime.now())
        self.date_due = self._compute_next_due_date()

    def __str__(self) -> str:
        completed_str = ', '.join(date.strftime("%Y-%m-%d") for date in self.completed_dates)
        return f"{self.title} - Recurring (Due: {self.date_due.date()}, Completed Dates: [{completed_str}], Interval: {self.interval.days} days)"


# Demonstration
if __name__ == "__main__":
    # Vehicle hierarchy 
    car = Car("Blue", 1500, 240, "SUV", max_range=450)
    electric = Electric("Green", 1200, 200, "Hatchback", battery_capacity=85, max_range=400)
    plane = Plane("White", 3000, 600, wingspan=25, seats=120)
    jet = Jet("Grey", 5000, 900, wingspan=35, engine_thrust=100)
    flying_car = FlyingCar("Red", 1800, 200, "Convertible", 22, seats=4)

    for vehicle in [car, electric, plane, jet, flying_car]:
        vehicle.move(100)

    # Polymorphic 
    generic_animal = Animal()
    for mover in [car, electric, plane, jet, flying_car, generic_animal]:
        mover.move(50)

    # ToDo task 
    rt = RecurringTask("Clean room", datetime.now(), timedelta(days=7))
    rt.mark_completed()
    print(rt)