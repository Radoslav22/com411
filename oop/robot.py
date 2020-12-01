class Robot:
    
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

    def grow(self):
      self.age = self.age + 1
      return self.age
  
    def __str__(self):
        return f"My name is {self.name} and I am {self.age} years old and my energy is {self.energy}"

    # An instance method
    def display(self):
        print(f"I am {self.name}")
  
    def eat(self,amount):
        potential_energy = self.energy + amount
        if(potential_energy > Robot.MAX_ENERGY):
            self.energy = Robot.MAX_ENERGY
        else:
            self.energy = potential_energy
    def move(self,distance):
        potential_energy = self.energy - distance
        if(potential_energy < 0):
            self.energy = 0
        else:
            self.energy = potential_energy
    
if (__name__ == "__main__"):
    robot = Robot()
    robot.display()
    Robot.the_laws()
    print(robot)
    robot.move(10)
    print(robot)
    robot.eat(5)
    print(robot)
