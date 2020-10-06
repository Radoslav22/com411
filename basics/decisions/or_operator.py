print("What type of adventure should I have?")
adventure = input() 
if ((adventure == "scary") or (adventure == "short")):
  print("\nEntering the dark forest!")
elif ((adventure == "safe") or (adventure == "long")):
  print("\nTaking the safe route!")
else:
  print("\nNot sure which route to take")