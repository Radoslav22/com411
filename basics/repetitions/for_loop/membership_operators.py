print("What phrase do you see?")
phrase = input()

print("\nReversing...\n\nThe phrase is: ", end="")

reversed = ""

for letter in phrase:
    reversed = letter + reversed

print(reversed) 