from human import Human
from robot import Robot

class Planet:
    
    def __init__(self):
        self.inhabitants = {
            'humans' :[],
            'robots':[]
            }
       
    
    def __repr__(self):
        return f"planet(humans = {self.inhabitants['humans']}, robots = {self.inhabitants['robots']})"
    
    def __str__(self):
        return f"This planet has {len(self.inhabitants['humans'])} humans and {len(self.inhabitants['robots'])} robots"
    
    #add human in the humans list    
    def add_human(self, human):
        self.inhabitants['humans'].append(human)
    #add robot in the robot list 
    def add_robot(self, robot):
        self.inhabitants['robots'].append(robot)
    #remove human from the humans list     
    def remove_human(self, human):
        self.inhabitants['humans'].remove(human)
        
    #remove robot from the robots list 
    def remove_robot(self, robot):
         self.inhabitants['robots'].remove(robot)
        
if (__name__ == "__main__"):
    planet=Planet()
    print(repr(planet))
    print(planet)
    rado = Human("Rado")
    planet.add_human(rado)
    print(repr(planet))
    print(planet)
