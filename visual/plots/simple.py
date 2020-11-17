import matplotlib.pyplot as plt
#create a program to display the path Beep and Bop are taking through Robo City
#first function
def display(x_values, y_values):
    plt.plot(x_values, y_values)
    plt.show()

#second function
def run():
    x_values = [1, 2, 3, 4, 5]
    y_values = [1, 4, 9, 16, 25]
    dis = display(x_values, y_values)

run()
