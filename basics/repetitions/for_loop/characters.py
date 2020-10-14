print("What strange markings do you see?")
marking = input() 
print("\nIdentifying...")
for count in range (0, len(marking), 1):
  print("index ", count,": ", (marking [count]))
print("\nDone!")