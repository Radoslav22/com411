class Human:
    MAX_ENERGY = 100
    # An initialiser (special instance method) 
    def __init__(self, name="Human", age = 0):
         # An instance attribute
         self.name = name
         self.age = age
         self.energy = Human.MAX_ENERGY
         
    def grow(self):
        self.age = self.age + 1
   
    #magic methods   
    def __str__(self):
        return f"My name is {self.name} and I am {self.age} years old and my energy is {self.energy}"
    
    def __repr__(self):
        return f"human(name={self.name}, age={self.age}, energy={self.energy})"
    def display(self):
        print(f"I am {self.name}")
    
    def eat(self, amount):
        if(self.energy + amount > Human.MAX_ENERGY):
            self.energy = Human.MAX_ENERGY
        else:
            self.energy += amount
    def move(self, distance):
        potential_energy = self.energy - distance
        if(potential_energy < 0):
            self.energy = 0
        else:
            self.energy = potential_energy

    
if (__name__ == "__main__"):
    human = Human()
    human.grow()
    human.display()
    print(human)
    print(repr(human))
    human.move(10)
    print(human)
    human.eat(5)
    print(human)
    
    