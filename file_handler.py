import csv


class FileHandler:
    def __init__(self, animal: str):
        self._animal = animal
        self.set_animal = animal
        self._filepath = f"data/{self._animal}.csv"

    @property
    def animal(self):
        return self._animal

    @animal.setter
    def set_animal(self, animal):
        if animal[-1] != "s":
            self._animal = animal + "s"
        else:
            self._animal = animal

    def load_file(self):
        animals = []
        try:
            with open(self._filepath) as file:
                data = csv.DictReader(file, delimiter=",", skipinitialspace=True)
                for line in data:
                    animals.append(line)
        except:
            print(f"Sorry, we don't have any {self.animal} here")
            return []

        return animals


if __name__ == "__main__":
    file_cats = FileHandler("cats")
    file_dogs = FileHandler("dogs")
    print(file_cats.load_file())
    print(file_dogs.load_file())
