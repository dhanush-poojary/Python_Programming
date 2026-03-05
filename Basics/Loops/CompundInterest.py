#Compound interest calculator
principal = 0
rate = 0
time = 0

while principal <=0 : 
  principal = float(input("Enter principal amount: "))
  if principal<=0:
    print("Principal amount cannot be Negetive or Zero")

while rate <=0 : 
  rate  = float(input("Enter rate of interest: "))
  if rate <=0:
    print("rate of interest cannot be Negetive or Zero")

while time <=0 : 
  time = int(input("Enter time amount: "))
  if time <=0:
    print("Time cannot be Negetive or Zero")

total = pow(principal*(1+rate/100),time)
print(f"The Final balance amount: {total:.2f}")