print("Where should I look?")
place = input()
if(place == "in the bedroom"):
  print("Where in the bedroom should I look?")
  place2 = input()
  if (place2 == "under the bed"):
    print("Found some shoes but no battery")
  else:
    print("Found some mess but no battery")
elif(place == "in the bathroom"):
  print("Where in the bathroom should I look?")
  place3 = input()
  if (place3 == "in the bathtub"):
    print("Found a rubber duck but no battery")
  else:
    print("Found some mess but no batteryFound a wet surface but no battery.")
elif(place == "in the lab"):
  print("Where in the lab should I look?")
  place4 = input()
  if (place4 == "on the table"):
    print("Yes! I found my battery!")
  else:
    print("Found some tools but no battery.")
else:
  print("I am not sure where that place is located.")



