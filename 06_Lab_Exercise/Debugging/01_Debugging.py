class Rocket:
    def __init__(self, thrust: int = 0) -> None:
        self.thrust = thrust
        self.altitude = 0
        self.duration = 0

    def boost(self) -> None:
        self.thrust += 10

    def decelerate(self) -> None:
        self.thrust = max(self.thrust - 10, 0)

    def launch_step(self) -> None:
        self.altitude += self.thrust
        self.duration += 1

    def average_climb_rate(self) -> float:
        return self.altitude / self.duration if self.duration > 0 else 0

if __name__ == '__main__':
    my_rocket = Rocket()
    print("Initiating rocket systems.")
    while True:
        action = input("Command? [B]oost, [D]ecelerate, show [A]ltitude, or show average climb [R]ate: ").upper()
        if action not in "BDAR" or len(action) != 1:
            print("Invalid command.")
            continue
        if action == 'B':
            my_rocket.boost()
            print("Boosting thrust.")
        elif action == 'D':
            my_rocket.decelerate()
            print("Reducing thrust.")
        elif action == 'A':
            print(f"Current altitude: {my_rocket.altitude} meters.")
        elif action == 'R':
            print(f"Average climb rate: {my_rocket.average_climb_rate():.2f} m/s.")
        my_rocket.launch_step()