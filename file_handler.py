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
        self._animals = []
        try:
            with open(self._filepath) as file:
                data = csv.reader(file, delimiter=",")
                line_count = 0
                for line in data:
                    if line_count == 0:
                        line_count += 1
                        continue
                    self._animals.append(line)
        except:
            print(f"Sorry, we don't have any {self.animal} here")
            return []

        return self._animals
