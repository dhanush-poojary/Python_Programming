#Concession Stand Program Using Dictionaries

menu = {"pizza":3.00,
        "popcorn":4.50,
        "fries":2.00,
        "chips":2.50,
        "soda":1.00,
        "coca cola":1.20 }
cart = []
total = 0

print("-----------Menu---------------")
for key,value in menu.items():
  print(f"{key:10}:${value:.2f}")
print("-------------------------------")

while(True):
 food = input("Choose an Item (x to Exit): ")
 if(food.lower() == "x"):
   break
 elif(not menu.get(food.lower())):
   print(f"{food} is Not available!!!")
 else:
   cart.append(food.lower())

print("-------------------------------")
print("Your Cart: \t\t")
for food in cart :
  total+= menu.get(food)
  print(food,end=" ,")

print()
print(f"Your total is: ${total:.2f}")
 