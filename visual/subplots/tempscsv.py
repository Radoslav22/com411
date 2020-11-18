import csv
import matplotlib.pyplot as plt

first_key=None
second_key=None
#The first function should be named read_data and should have 0 parameters
def read_data():
    global first_key, second_key
    #read the file and store its contents into a dictionary
    with open("C:/Users/Radoslav/Desktop/problem solving trough programming/com411/visual/subplots/temps.csv") as csv_file:
        #read the csv file
        csv_reader = csv.reader(csv_file) 
        #start reading from next line, pass week1 and week 2
        header = next(csv_reader)
        #to do not strip everywhere
        first_key = header[0].strip()
        second_key = header[1].strip()
        #make dictionary
        data = {first_key : [], second_key : []}
        for row in csv_reader:
            data[first_key].append(row[0].strip())
            data[second_key].append(row[1].strip())
            
        #return the dictionary
        return data
# the second function with 0 parameters
def run():
    #calling the first function and storing the resulting dictionary in a local variable named data.
    data = read_data()
    #2 subplots arranged vertically and share x 
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex='all')
    # The first subplot should show a plot for week1
    ax1.plot (data[first_key])
    #the second subplot should show a plot for week2.
    ax2.plot (data[second_key])
    #show the diagrams
    plt.tight_layout()
    plt.show()
    
#call the second function
run()
    
    
            
            

