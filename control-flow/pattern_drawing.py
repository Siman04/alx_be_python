input = int(input("Enter the size of the pattern:"))
if input > 0:
 row = 0 
 while row < input:
  for column in range(input):
   print("*", end="")
  print()
  row += 1