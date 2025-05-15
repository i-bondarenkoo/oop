class Robot:
    def __init__(self, name, model):
        self.name = name
        self.__model = model

    def greet(self):
        return f"Привет, я {self.name}, модель {self.__model}"

    def make_sound(self):
        return f"Bi-bi"

    # сеттер для установки модели
    def set_model(self, model):
        if not isinstance(model, str):
            raise ValueError(f"Значение атрибута {self.__model} должно быть строкой")
        elif len(model) < 5:
            raise ValueError("Название модели слишком короткое")
        self.__model = model
        return f"Вы успешно изменили модель вашего робота"

    # геттер для получения/прочтения данных объекта
    def get_model(self):
        return self.__model

    def action(self):
        return f"Чинит систему"

    @classmethod
    def create_default(cls):
        return cls("Безымянный", "Базовая")

    @staticmethod
    def validate_name(name):
        return True if name is not None and len(name) > 2 else False

    def __str__(self):
        return f"Робот {self.name}, модель робота - {self.__model}"


class WarRobot(Robot):
    def __init__(self, name, model, weapon):
        super().__init__(name, model)
        self.weapon = weapon

    def make_sound(self):
        return f"Pay-pay"

    def action(self):
        return f"Атакует {self.weapon}"


class RobotDog(Robot):
    def __init__(self, name, model, breed):
        super().__init__(name, model)
        # порода
        self._breed = breed

    def make_sound(self):
        return f"Gav-gav"

    def fetch(self, item):
        return f"{self.name} принес {item}"

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if not isinstance(value, str):
            raise ValueError("Порода должна быть строкой")
        if len(value) < 3:
            raise ValueError("Название породы слишком короткое")
        self._breed = value

    @staticmethod
    def validate_name(name):
        if len(name) < 4:
            raise ValueError("Имя должно быть длиннее 4 символов")

        return Robot.validate_name(name)

    def action(self):
        return f"Ищет взрывчатку"

    def __str__(self):
        return f"Собака-робот {self.name}, порода: {self._breed}"


if __name__ == "__main__":
    # robot1 = Robot("Бамбалби", "GT-504")
    # print(robot1.greet())
    # print(robot1.make_sound())
    # warrior1 = WarRobot("Терминатор", "GT-509", "Револьвер")
    # print(warrior1.greet())
    # print(warrior1.make_sound())
    # print(robot1.set_model("Боевой робот"))
    # print(robot1.get_model())
    # print(Robot.create_default())
    # print(Robot.validate_name("Р2"))
    # robots = [
    #     Robot("R2-D2", "Астромеханик"),
    #     WarRobot("T-800", "Терминатор", "Плазмаган"),
    #     RobotDog("Бобик", "Пес-охранник", "овчарка"),
    # ]
    # for elem in robots:
    #     print(elem.greet())
    #     print(elem.make_sound())
    # robot_dog1 = RobotDog("Бобик", "Пес-охранник", "овчарка")
    # print(robot_dog1.validate_name("имя123"))
    # robot_zoo = [
    #     Robot("R2-D2", "Астромеханик"),
    #     WarRobot("T-800", "Терминатор", "Лазер"),
    #     RobotDog("Бобик", "Пёс-охранник", "Доберман"),
    # ]
    # for robot in robot_zoo:
    #     print(robot.greet())
    #     print(robot.action())
    #     print(robot.make_sound())
    #     if isinstance(robot, RobotDog):
    #         print(robot.fetch("палку"))
    dog = RobotDog("Бобик", "Охранник", "Доберман")
