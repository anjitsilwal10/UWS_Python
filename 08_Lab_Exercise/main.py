from abc import ABC, abstractmethod
from random import randint

# Exercise 1: Tuples - Swap values

def tuple_swap_demo():
    print("Exercise 1: Tuple Swap")
    a, b = 5, 10
    print(f"Before swap: a = {a}, b = {b}")
    a, b = b, a  # Tuple unpacking swap
    print(f"After swap: a = {a}, b = {b}\n")

# Exercise 2: Sets - Find intersection
def set_intersection_demo():
    print("Exercise 2: Set Comparison")
    set1 = {"Tom", "Jerry", "Hewey", "Dewey", "Louie"}
    set2 = {"Tom", "Garfield", "Snoopy", "Hewey", "Dewey"}
    common_names = set1.intersection(set2)
    print("Names in both sets:", common_names, "\n")


# Exercise 3: Dictionaries - Histogram

def histogram(data: list) -> dict:
    result = {}
    for item in data:
        result[item] = result.get(item, 0) + 1
    return result

def histogram_demo():
    print("Exercise 3: Histogram from List")
    my_list = [1, 2, 3, 1, 2, 3, 4]
    print("List:", my_list)
    print("Histogram:", histogram(my_list), "\n")

# Exercise 4: Abstract Classes - Dice
class Dice(ABC):
    def __init__(self):
        self.face = None

    @abstractmethod
    def roll(self) -> int:
        pass

class SixSidedDice(Dice):
    def roll(self) -> int:
        self.face = randint(1, 6)
        return self.face

class TenSidedDice(Dice):
    def roll(self) -> int:
        self.face = randint(1, 10)
        return self.face

def dice_roll_demo(dice: Dice, rolls: int):
    print(f"Rolling {dice.__class__.__name__} {rolls} times")
    results = [dice.roll() for _ in range(rolls)]
    stats = histogram(results)
    print("Histogram of rolls:", stats, "\n")


def main():
    tuple_swap_demo()
    set_intersection_demo()
    histogram_demo()

    # Dice simulations
    dice_roll_demo(SixSidedDice(), 1000)
    dice_roll_demo(TenSidedDice(), 1000)

if __name__ == "__main__":
    main()