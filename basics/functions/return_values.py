#function for calculating the total weight of the two bots.
def sum_weights (Bop_weight, Beep_weight):
    total_weight = Bop_weight + Beep_weight
    return total_weight
#function for average weight for both of the bots
def calc_avg_weight (Bop_weight, Beep_weight):
    avg_weight = (Bop_weight + Beep_weight) / 2
    return avg_weight
#function for the user to enter the weight for each bot
def run ():
    print("\nWhat is the weight of Bop?")
    bop_weight = float(input())
    print("\nWhat is the weight of Beep?")
    beep_weight = float(input())
    print("\nWhat would you like to calculate (sum or average)?")
    action = input()

    if (action == "sum"):
        answer = sum_weights(beep_weight, bop_weight)
        print ("\nThe sum of Beep and Bop's weight is: {}".format(answer))
    elif (action == "average"):
        answer = calc_avg_weight(beep_weight, bop_weight)
        print ("\nThe average of Beep and Bop's weight is: {}".format(answer))
    else:
        print("\nI am not sure what you would like to do.")
#call the function
run()

