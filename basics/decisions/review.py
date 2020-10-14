print("\nWhat brand is your car?")
brand = input() 
if ((brand == "bmw") or (brand == "vw") or (brand == "mercedes") or (brand == "audi")):
   print("\nDoes your brand made in Germany?")
   response = input()
   if ((response == "yes") or (response == "yep")):
     print("\nOhh, you have a nice car from German!")
   else:
      print("\nSearch in google!")
elif ((brand == "ford") or (brand == "chevrolet") or (brand == "dodge")):
   print("\nDoes your car made in America?")
   response2 = input() 
   if((response2 == "yes") or (response2 == "yep")):
     print("\nI like American muscles!")
   else:
       print("\nSearch in google!")
elif ((brand == "bentley") or (brand == "jaguar") or (brand == "mini")):
  print("\nDoes your car made in UK?")
  response3 = input() 
  if((response3 == "yes") or (response3 == "yep")):
    print("\nUK cars are the best!")
  else:
      print ("\nSearch in google!")
else:
  print("\nI cannot recognise this brand")
print("\nDoes your car with left hand drive or right?")
direction = input()
print("\nWhere are you from?(eu,uk)")
country = input()
if ((direction == "left") and (country == "eu")):
  print("\nYou are with the correct direction!")  
elif ((direction == "right") and (country == "eu")):
  print("\nYou are with the incorrect direction!")
elif ((direction == "left") and (country == "uk")):
  print("\nYou are with the incorrect direction!") 
elif ((direction == "right") and (country == "uk")):
  print("\nYou are with the correct direction!") 
else:
  print("\nI don't know what you mean")   