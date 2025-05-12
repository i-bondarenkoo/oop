class Person:
    def __init__(self, first_name, last_name, age):
        self._first_name = first_name
        self._last_name = last_name
        self.__age = age

    def set_age(self, age):
        if age < 1 or age > 120:
            raise ValueError(f"Возвраст должен быть от 1 до 120")
        self.__age = age

    def describe(self):
        print(f"Я {self._first_name} {self._last_name}, мне {self.__age} лет")


if __name__ == "__main__":
    ivan = Person("Иван", "Иванов", 20)
    ivan.set_age(23)
    ivan._Person__age = 60
    ivan.describe()
    print(ivan._Person__age)
