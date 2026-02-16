#basic calculator
a = float(input("Enter the first number: "))
op = input("Enter the operator: ")
b = float(input("Enter the second number: "))

if(op == "+"):
   print(f"addition of {a} + {b} = {a+b}")
elif(op == "-"):
   print(f"addition of {a} - {b} = {a-b}")
elif(op == "*"):
 print(f"addition of {a} * {b} = {a+b}")
elif(op == "/"):
   print(f"addition of {a} / {b} = {a+b}")
elif(op == "%"):
    print(f"addition of {a} % {b} = {a%b}")
else:
  print("Enter the valid operator!")