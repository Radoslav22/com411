#create a program to help Beep and Bop decide which steps to take.
#first function
def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    #the function return the step with the smallest likelihood of falling
    return min(likelihoods)
#second function
def run():
    #The function call the first function and stored the returned value in a local variable
    min_likelihood = likelihood ()
    print("Minimum likelihood of falling: {}%".format(min_likelihood))
#call the second function
run()