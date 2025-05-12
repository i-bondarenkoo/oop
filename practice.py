class Animal:
    def __init__(self, name, species):
        if not isinstance(name, str) or not isinstance(species, str):
            raise ValueError("Имя и вид должны быть строками")
        self.__name = name
        self.__species = species

    def get_info(self):
        return f"Имя: {self.__name}, Вид: {self.__species}"

    def make_sound(self):
        return f"Животное издает звук"

    @staticmethod
    def is_animal(obj):
        return isinstance(obj, Animal)

    def set_name(self, new_name):
        if not isinstance(new_name, str):
            raise ValueError("Имя должно быть строкой")
        self.__name = new_name
        return f"Имя успешно изменено на: {self.__name}"


class Bird(Animal):
    def __init__(self, name, species, wingspan):
        super().__init__(name, species)
        # размах крыльев
        self.wingspan = wingspan

    def make_sound(self):
        return f"Чик-чирик!"

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["species"], data["wingspan"])

    def get_info(self):
        return f"Имя: {self.__name}, Вид: {self.__species}, Размах крыльев: {self.wingspan} см"


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def show_animals(self):
        pass

    def make_all_sounds(self):
        for animal in self.animals:
            print(animal.make_sound())


tiger = Animal("Ричард", "Тигр")
print(tiger.get_info())
print(tiger.is_animal(tiger))
tiger2 = Animal("Ронни", "Тигр")
print(tiger.set_name("123"))
print(tiger._Animal__name)
