#create a program to help Beep and Bop record what they can see in the distance.
#function one set of observation
def observed ():
    observations = set(["Flying Car", "Sky Scraper", "Laser", "Dome"])
    #return the set 
    return observations 
#call the first function into a second
def run ():
    record  = observed () 
    print (record)
# call the second function
run()
