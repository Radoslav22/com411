#We wish to create a program to display information about the current working folder.
#The first function
def cwd():
    import os
    path = os.getcwd()
    print(f"The current Working Folder: {path}")
    print("The folder contains the following:")
    for file in os.listdir(path):
        print(file)
#second function
def run ():
    print("Processing...")
    #call the first function
    cwd()

run()