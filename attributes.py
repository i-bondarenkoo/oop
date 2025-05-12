class BlueCat:
    # парода
    # атрибут класса
    breed = "Russian Blue"
    names = []
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        BlueCat.increment_count()

    def meow(self):
        print(f"{self.name} of {self.breed} says: Meow!")

    @classmethod
    def increment_count(cls):
        cls.count += 1

    @classmethod
    def make_cat(cls, name):
        if name == "Tom":
            return cls("Tom", 2)
        elif name == "Angela":
            return cls("Angela", 1)
        return cls("Ginger", 1)

    @staticmethod
    def get_human_age(age):
        return age * 8


if __name__ == "__main__":
    tom = BlueCat.make_cat("Tom")
    angela = BlueCat.make_cat("Angela")
    tom.meow()
    angela.meow()
    print(angela.get_human_age(angela.age))
