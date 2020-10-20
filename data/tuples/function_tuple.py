#Program to display minimum and maximum 
#first function
def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    #the function return the step with the smallest likelihood of falling
    return min(likelihoods), max(likelihoods)
#second function
def run():
    #The function call the first function and stored the returned value in a local variable
    values_likelihood = likelihood ()
    print("Minimum likelihood of falling: {}%".format(values_likelihood[0]))
    print("Maximum likelihood of falling: {}%".format(values_likelihood[1]))
#call the second function
run()