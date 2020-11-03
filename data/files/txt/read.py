#We wish to create a program to help Beep and Bop search the library
#The first function
def search (filepath):
    print("Searching...")
    
    with open(filepath) as file:
        for line in file:
            print(f"Looked in {line}", end = "")  
        
        print("...Done!")

#second function 
def run():
    search("data/files/txt/locations.txt")

#call the second function
run()