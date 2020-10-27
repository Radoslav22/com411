#We wish to create a program to help Beep and Bop identify the patterns.
#first function with no parameters 
def short_pattern():
    #make a dictionary
    pattern = {"sequence":"101", "occurrences":5}
    #return the dictionary
    return pattern
#second function with no parameters
def medium_pattern ():
    #make a dictionary
    pattern = {"sequence":"111000", "occurrences": 25}
    #return the dictionary
    return pattern
#third function with no parameters
def long_pattern():
     #make a dictionary
    pattern = {"sequence":"1100110011001100", "occurrences":50}
    #return the dictionary
    return pattern
#fourth function with no parameters
def run():
    print("Analysing patterns...")
    patterns = {"short sequence":short_pattern(), 
                "medium sequence": medium_pattern(), 
                "long sequence":long_pattern()}
    print(patterns)

#call the fourth function
run()
    
