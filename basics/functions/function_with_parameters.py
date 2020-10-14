#program to help Beep and Bop climb the bridge ladder.
def climb_ladder (remaining_steps, crossed_steps):
    #Compare the values of the two parameters
    if (remaining_steps > crossed_steps):
        print("Still some way to go!")
    else:
        print("We are almost there!")
#calls of the function
climb_ladder(5, 2)
climb_ladder(2, 5) 