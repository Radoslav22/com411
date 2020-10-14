print("How many bars should be charged?")
bars = int(input())

bars_charging = 0
print() 
while (bars > bars_charging):
  bars_charging = bars_charging + 1
  print("Charging:", "█" * bars_charging)
print("\nThe battery is fully charged.")