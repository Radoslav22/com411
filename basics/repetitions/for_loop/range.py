print("What level of brightness is required?")
brightness = int(input())

print("\nAdjusting brightness...\n")

for brightness_ in range(2, brightness + 1, 2):
    print("Beep's brightness level:", "*" * brightness)
    print("Bop's brightness level:", "*" * brightness)
    
print("\nAdjustments complete!")