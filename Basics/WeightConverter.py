#weight converter from KG to Pound
weight = float(input("Enter the weight: "))
unit = input("Enter Kilograms or pounds (K or P): ")

if(unit == "k"):
  weight*=2.205
  print(f"Kilograms -> Pound : {round(weight , 2)}Lbs")
elif(unit == "P"):
  weight/=2.205
  print(f"Pound -> Kilograms : {round(weight , 2)}Kgs")
else:
    print("Enter a valid unit of weight!")
