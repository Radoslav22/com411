from inhabitant import Inhabitant

class Human(Inhabitant):
    MAX_ENERGY = 100
    # An initialiser (special instance method) 
    def __init__(self, name="Human", age = 0):
         # An instance attribute
         self.name = name
         self.age = age
         self.energy = Human.MAX_ENERGY
         
   
    #magic methods   
    def __str__(self):
        return f"My name is {self.name} and I am {self.age} years old and my energy is {self.energy}"
    
    def __repr__(self):
        return f"human(name={self.name}, age={self.age}, energy={self.energy})"
    

    
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
    
    