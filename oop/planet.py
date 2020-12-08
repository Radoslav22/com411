from human import Human
from robot import Robot
from inhabitant import Inhabitant

class Planet:
    
    def __init__(self):
        self.inhabitants = []
       
    
    def __repr__(self):
        return f"planet(humans = {self.inhabitants}, robots = {self.inhabitants})"
    
    def __str__(self):
        num_human = 0
        num_robot = 0
        
        for inhabitant in planet.inhabitants:
            if isinstance(inhabitant, Human):
                num_human += 1

                
            elif isinstance(inhabitant, Robot):
                num_robot +=1
                
        
                
        return f"Found {num_human} humans and {num_robot} robots"
    
    #add human in the humans list    
    def add_inhabitant(self, inhabitant):
        self.inhabitants.append(inhabitant)
    
        
    #remove robot from the robots list 
    def remove_inhabitant(self, inhabitant):
         self.inhabitants.remove(inhabitant)
         
    

        
if (__name__ == "__main__"):
    planet=Planet()
    print(repr(planet))
    print(planet)
    rado = Human("Rado")
    poli = Robot("Poli")
    planet.add_inhabitant(rado)
    planet.add_inhabitant(poli)
    print(repr(planet))
    print(planet)
