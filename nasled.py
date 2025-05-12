class Employee:
    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def calculate_total_bonus(self):
        return self.salary // 100 * self.bonus

    def __str__(self):
        return f"{self.__class__.__name__} {self.name}, зарплата={self.salary}, премия={self.bonus}, премия в реблях={self.calculate_total_bonus()} рублей"


class Cleaner(Employee):
    def __init__(self, name):
        super().__init__(name, 15000, 1)


class Manager(Employee):
    def __init__(self, name):
        super().__init__(name, 45000, 15)


class CEO(Employee):
    def __init__(self, name):
        super().__init__(name, 105000, 100)

    def calculate_total_bonus(self):
        return 200000


def calc_bonuses(employees: list[Employee]):
    for employee in employees:
        print(
            f"Calc bonus for {employee.name}, it is = {employee.calculate_total_bonus()}"
        )


if __name__ == "__main__":
    masha = Cleaner("Maria Ivanovna")
    print(masha)
    grisha = Manager("Grigory Petrovich")
    print(grisha)
    ivan_palych = CEO("Ivan Pavlovych")
    print(ivan_palych)
    a_list = [masha, grisha, ivan_palych]
    calc_bonuses(a_list)
