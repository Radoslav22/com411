#The program should consist of the following three functions:
#first function 
def directions():
    #list 
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    #return list 
    return directions
#second function 
def menu ():
    print("Please select a direction:")
    dirs = directions ()
    #use a loop to display each direction in the list with an index number
    for index in range (len(dirs)):
        print ("{}: {}".format(index, dirs[index]))  
    #user input
    move_direction = int(input()) 
    #return the user input
    return dirs[move_direction]
# third function
def run ():
    route = []
    print("Working out escape route...")
    for count in range (5):
        direction = menu()
        route.append(direction)
    print("Escape route: {}".format(route))

run()