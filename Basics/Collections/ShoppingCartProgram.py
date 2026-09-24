#Shopping cart program
foods = []
prices = []
total = 0
print("----------Menu-------------")
print("""
         Pizza -- $21.2
         Burger -- $22.55
         Fries -- $15.6
         Coca Cola --$9.75
""")
while True :
   food = input("Enter a food to buy (x to Exit): ")
   if(food.lower() == "x"):
      break
   else:
      price = float(input(f"Enter the price of a {food}: "))
      foods.append(food)
      prices.append(price)

print("----------Your cart-------------\n")
amt = 0
for fp in foods,prices:
   print(fp,end="")
   
for i in prices:
   amt+=i
print(f"Your Total is = {amt}")