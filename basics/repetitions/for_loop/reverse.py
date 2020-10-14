print("What phrase do you see?")
phrase = input() 
print("\nReversing...\nThe phrase is: ",end = "")
for reverse in range (len(phrase) - 1, -1, -1):
  print(phrase[reverse],end = "")