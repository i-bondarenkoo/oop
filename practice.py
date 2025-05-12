class Robot:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def greet(self):
        return f"Привет, я {self.name}, модель {self.model}"

    def make_sound(self):
        return f"Bi-bi"


class WarRobot(Robot):
    def __init__(self, name, model, weapon):
        super().__init__(name, model)
        self.weapon = weapon

    def make_sound(self):
        return f"Pay-pay"


robot1 = Robot("Бамбалби", "GT-504")
print(robot1.greet())
print(robot1.make_sound())
warrior1 = WarRobot("Терминатор", "GT-509", "Револьвер")
print(warrior1.greet())
print(warrior1.make_sound())
