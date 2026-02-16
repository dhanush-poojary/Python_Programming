#weight converter from fahrenheit to celsius
degree = float(input("Enter the Degree: "))
unit = input("Enter fahrenheit or celsius (F or C): ")

if(unit == "F"):
  degree = (degree - 32) * 5/9 
  print(f"fahrenheit to celsius : {round(degree , 2)}°C")
elif(unit == "C"):
  degree= (degree * 9/5) + 32 
  print(f"celsius to fahrenheit : {round(degree , 2)}°F")
else:
    print("Enter a valid unit of degree!")
