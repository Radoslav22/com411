print("Program Started!")
print("Please enter a standart character.")
#
letter = input()
if (len(letter)) == 1:
  print("The ASCII code for {} is: {}.".format(letter,(ord(letter))))
else:
  print("This is not a standart character.")
print("Program ended!")
