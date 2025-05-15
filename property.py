class Cat:
    __slots__ = ("_name", "_age")

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # геттер
    @property
    def name(self):
        return self._name

    # сеттер
    @name.setter
    def name(self, value):
        if not value:
            raise AttributeError("Имя не может быть пустым")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 1 or value > 15:
            raise AttributeError("Возраст должен быть в промежутке 1-15")
        self._age = value

    def __repr__(self):
        return f"Cat(name={self.name}, age={self.age})"

    # def __setattr__(self, key, value):
    #     if key not in self.FIELDS:
    #         raise AttributeError(f"Допустимые атрибуты {self.FIELDS}")
    #     if key == "name" and not value:
    #         raise AttributeError("Имя не может быть пустым")
    #     if key == "age" and (value < 1 or value > 15):
    #         raise ArithmeticError("Возраст объекта должен быть в диапазоне 1-15")
    #     self.__dict__[key] = value


if __name__ == "__main__":
    tom = Cat("Tom", 2)
    print(tom)
