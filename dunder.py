class Banknote:
    def __init__(self, value: int):
        self.value = value

    # красивый вывод, репр для программистов, стр для пользователей
    def __repr__(self):
        return f"Banknote({self.value})"

    def __str__(self):
        return f"Банкнота номиналом в {self.value} рублей"

    def __eq__(self, other):
        if other is None or not isinstance(other, Banknote):
            return False
        return self.value == other.value

    # lt - less than меньше чем
    def __lt__(self, other):
        # тут нужно так же проверить тип как в eq
        return self.value < other.value

    # greater than
    def __gt__(self, other):
        return self.value > other.value

    def __le__(self, other):
        return self.value <= other.value

    def __ge__(self, other):
        return self.value >= other.value


class Iterator:
    def __init__(self, container):
        self.container = container
        self.index = 0

    def __next__(self):
        if 0 <= self.index < len(self.container):
            value = self.container[self.index]
            self.index += 1
            return value
        raise StopIteration


class Wallet:
    def __init__(self, *banknotes: Banknote):
        self.container = []
        self.container.extend(banknotes)
        self.index = 0

    def __repr__(self):
        return f"Wallet ({self.container})"

    def __contains__(self, item):
        return item in self.container

    def __bool__(self):
        return len(self.container) > 0

    def __len__(self):
        return len(self.container)

    def __call__(self):
        return f"{sum(e.value for e in self.container)} рублей"

    def __iter__(self):
        return Iterator(self.container)

    def __getitem__(self, item: int):
        if item < 0 or item > len(self.container):
            raise IndexError
        return self.container[item]

    def __setitem__(self, key: int, value: Banknote):
        if key < 0 or key > len(self.container):
            raise IndexError
        self.container[key] = value


if __name__ == "__main__":
    banknote = Banknote(50)
    fifty = Banknote(50)
    hundred = Banknote(100)
    wallet = Wallet(fifty, hundred, hundred)
    wallet[0] = Banknote(500)
    for money in wallet:
        print(money)
