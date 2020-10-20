#first function
def directions ():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions 
#second function
def menu ():
    print ("Please select a direction:")
    dirs = directions ()
    for index in range (len(dirs)):
        print("{}: {}".format(index, dirs[index]))
#third function
def run():
    menu()

run()