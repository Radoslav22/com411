print("Program Started!")
print("Please enter an ASCII code:")
code = abs(int(input()))

if (code in range  (32,127)):
  print("The character represented by the ASCII code {} is {}.".format(code,chr(code)))
else:
  print("This is not a valid ASCII code!")
print("Program Ended!")