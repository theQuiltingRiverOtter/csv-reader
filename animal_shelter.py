from file_handler import FileHandler
from animals import Animal, Cat, Dog


class AnimalShelter:
    def __init__(self):
        self._animals = []

    def get_animals(self):
        animal_name = input("Please enter an animal name: ").lower()
        self._file = FileHandler(animal_name)
        animals = self._file.load_file()
        for animal in animals:
            if animal_name == "cats" or animal_name == "cat":
                self._animals.append(Cat(animal))
            elif animal_name == "dog" or animal_name == "dogs":
                self._animals.append(Dog(animal))
            else:
                self._animals.append(Animal(animal))

    def print_animals(self):
        for animal in self._animals:
            print(animal)


if __name__ == "__main__":
    megans_animal_shelter = AnimalShelter()
    megans_animal_shelter.get_animals()
    megans_animal_shelter.get_animals()
    megans_animal_shelter.print_animals()
