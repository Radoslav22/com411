#program to help Bop climb the bridge ladder.
#function for representing the number of steps on the ladder
def display_ladder (steps):
    for step in range (steps):
        print("| |")
        print("***") 
    # Display bottom of ladder
    print("| |")
#function to ask the user for the number of steps
def create_ladder():
    print("How many steps remain?")
    steps = int(input())
    display_ladder(steps)

create_ladder()