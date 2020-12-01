from planet import Planet
from human import Human
from robot import Robot
import random

class Universe:
    
    def __init__(self):
        self.planets = []
    
    def __repr__(self):
        return f"universe(planets={self.planets}"
    def __str__(self):
        return f"The universe contains {len(self.planets)} planets."
        
    def generate(self):
        #create a new planet 
        planet = Planet()
        
        #populate with random humans and robots
        for index in range(random.randint(1, 10)):
            robot = Robot(f"Robot{index}")
            planet.add_robot(robot)
        
        for index in range(random.randint(1, 10)):
            human = Human(f"Human{index}")
            planet.add_human(human)
            
        #add to list of planets
        self.planets.append(planet)
        
if (__name__ == "__main__"):
    universe = Universe()
    universe.generate()
    print(repr(universe))
    print(universe)
        

