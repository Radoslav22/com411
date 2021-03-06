from abc import ABC

class Inhabitant(ABC):

    MAX_ENERGY = 100

    def __init__(self, name="Inhabitant", age=0, energy=MAX_ENERGY):
        self.name = name
        self.age = age
        self.energy = Inhabitant.MAX_ENERGY

    def grow(self):
        self.age = self.age + 1
        
    def display(self):
        print(f"I am {self.name}")
    
    def eat(self, amount):
        if(self.energy + amount > Inhabitant.MAX_ENERGY):
            self.energy = Inhabitant.MAX_ENERGY
        else:
            self.energy += amount
    def move(self, distance):
        potential_energy = self.energy - distance
        if(potential_energy < 0):
            self.energy = 0
        else:
            self.energy = potential_energy
