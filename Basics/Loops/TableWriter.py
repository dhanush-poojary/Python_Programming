# printing a table 
x = int(input("Enter the number to print the table of: "))
i = 1
while i<=10:
  print(f"{x:2d} X {i:2d} = {x*i:2d}")
  i+=1


#Printing Table Upside Down but with same loop
# x = int(input("Enter the number to print the table of: "))
# i = 1
# while i<=10:
#   print(f"{x:2d} X {10-i+1:2d} = {x*(10-i+1):2d}")
#   i+=1
