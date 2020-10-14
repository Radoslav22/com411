print("How many numbers should I sum up?")
numbersum = int(input())

summed = 1
total = 0
while (summed < numbersum):
    print("Please enter number", summed, "of", numbersum, ":")
    number = int(input())
    total = total + number
    summed = summed + 1
print("The answers is", total)