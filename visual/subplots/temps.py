import matplotlib.pyplot as plt
#The first function should be named read_data and should take 1 parameter that represents a file path and name.
def read_data (file_path):
    #The function should start by opening the specified file in read mode.
    values = []
    with open(file_path) as file:
        #The function should then read each line in the file and store it into a list
        for line in file.readlines():
            print(f"{line.strip()}")
            values.append(float(line.strip()))
    #return the list of values       
    return values

#The second function should be name run and should take 0 parameters.
def run():
    data = read_data("C:/Users/Radoslav/Desktop/problem solving trough programming/com411/visual/subplots/temps.txt")
    fig, (ax1, ax2) = plt.subplots(1, 2)
        
    ax1.plot(range(1, 8), data)
    ax2.bar(range(1, 8), data)
    
    plt.xlabel("day")
    plt.ylabel("temperature")
    plt.tight_layout()
    plt.show()
    
run()
