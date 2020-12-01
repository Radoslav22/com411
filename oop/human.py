class Robot:

  # A class attribute
  laws = "Protect, Obey and Survive"

  # A class method
  def the_laws():
    print(Robot.laws)

  # An initialiser (special instance method)
  def __init__(self):

    # An instance attribute
    self.name = "Robot"
    self.age = 0

  def grow(self):
      self.age = self.age + 1
      return self.age
  
  def __str__(self):
     return f"My name is {self.name} and I am {self.age} years old."

  # An instance method
  def display(self):
    print(f"I am {self.name}")
    
if (__name__ == "__main__"):
    robot = Robot()
    robot.display()
    Robot.the_laws()
    robot.__str__()
    
class Human:
    MAX_ENERGY = 100
     
    def __init__(self):
         
         self.name = "Human"
         self.age = 0
         self.energy = Human.MAX_ENERGY
         
    def grow(self):
        self.age = self.age + 1
         
    def display(self):
        print(f"I am {self.age}")
        
    def __str__(self):
        return f"My name is {self.name} and I am {self.age} years old."

    
if (__name__ == "__main__"):
    human = Human()
    human.grow()
    human.display()
    human.__str__()
    