from inhabitant import Inhabitant 

class Robot(Inhabitant):
    
    MAX_ENERGY = 100  
    # A class attribute
    laws = "Protect, Obey and Survive"

    # A class method
    def the_laws():
        print(Robot.laws)

    # An initialiser (special instance method)
    def __init__(self, name="Robot", age = 0):

        # An instance attribute
        self.name = name
        self.age = age
        self.energy = Robot.MAX_ENERGY

  
    def __str__(self):
        return f"My name is {self.name} and I am {self.age} years old and my energy is {self.energy}"
    
    def __repr__(self):
        return f'robot(name={self.name}, age={self.age}, energy={self.energy})'

    
if (__name__ == "__main__"):
    robot = Robot()
    robot.display()
    Robot.the_laws()
    print(robot)
    robot.move(10)
    print(robot)
    robot.eat(5)
    print(robot)
