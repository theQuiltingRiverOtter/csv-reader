class Animal:
    def __init__(self, name: str, age: int, breed: str) -> None:
        self.set_name = name
        self.set_age = age
        self.set_breed = breed
        self._notes = []

    def __str__(self):
        return f"{self.name.title()} is a {self.age} year old {self.breed}"

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def breed(self):
        return self._breed

    @name.setter
    def set_name(self, name: str):
        if type(name) != str:
            raise TypeError("name must be a string")
        if len(name) >= 2:
            self._name = name
        else:
            raise ValueError("name must be at least two characters long")

    @age.setter
    def set_age(self, age: int):
        if type(age) != int:
            raise TypeError("age must be an integer")
        if age < 0:
            raise ValueError("Please enter a positive integer")
        else:
            self._age = age

    @breed.setter
    def set_breed(self, breed: str):
        if type(breed) != str:
            raise TypeError("name must be a string")
        else:
            self._breed = breed

    def add_note(self, note: str):
        self._notes.append(note)


class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age, breed)

    def __str__(self):
        return f"{self.name.title()} is a {self.age} year old {self.breed} dog"


class Cat(Animal):
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age, breed)

    def __str__(self):
        return f"{self.name.title()} is a {self.age} year old {self.breed} cat"
