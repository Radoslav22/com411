print("How many rows should I have?")
rows = int(input())
print("How many columns should I have?")
colums = int(input())
print("\nHere I go:\n\n", end = "")
for columss in range (0,colums,1):
  for rowss in range (0,rows,1):
    print(":-)", end="")
  print() 
print("\nDone!")

