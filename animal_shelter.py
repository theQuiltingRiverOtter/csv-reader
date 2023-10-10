from file_handler import FileHandler
from animals import Animal, Cat, Dog


class AnimalShelter:
    def __init__(self):
        self._animals = []

    def get_animals(self):
        animal = input("Please enter an animal name: ")
        self._file = FileHandler(animal)
        animals = self._file.load_file()
        for animal in animals:
            self._animals.append(Animal(animal[0], int(animal[1]), animal[2]))

    def print_animals(self):
        for animal in self._animals:
            print(animal)


megans_animal_shelter = AnimalShelter()
megans_animal_shelter.get_animals()
megans_animal_shelter.print_animals()
