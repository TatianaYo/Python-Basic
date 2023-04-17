"""
Доработаем задачи 5. Создайте класс-фабрику. Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
"""


class AnimalFabric:
    def make_animal(self, animal_type: str, *args, **kwargs):
        new_animal = self.get_maker(animal_type)
        return new_animal(*args, **kwargs)

    def get_maker(self, animal_type: str):
        types = {"birds": Birds, "fishes": Fishes, "reptiles": Reptiles}
        return types[animal_type.lower()]


class Fauna(AnimalFabric):

    def __init__(self, name: str, blood_color: str):
        self.name = name
        self.blood_color = blood_color

    def eat(self):
        print('Need food')


class Birds(Fauna):

    def __init__(self, name: str, blood_color: str, feathers: bool):
        super().__init__(name, blood_color)
        self.feathers = feathers

    def fly(self):
        print('I can fly!')


class Fishes(Fauna):
    def __init__(self, name: str, blood_color: str, gills: bool):
        super().__init__(name, blood_color)
        self.gills = gills


class Reptiles(Fauna):
    def __init__(self, name: str, blood_color: str, scales: bool):
        super().__init__(name, blood_color)
        self.scales = scales


fabric = AnimalFabric()
animal_from_fabric = fabric.make_animal("fishes", "dori", "blue", True)
print(animal_from_fabric)
