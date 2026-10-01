#Exception means run time errors
try:
    n = int(input("Enter the number for divider by: "))
    print(12//n)
except ValueError:
    print("[Value Error] Only Integer Value ")
except ZeroDivisionError:
    print("Division by Zero")
except Exception as e:
    print(e)
else:
    #it will execute after either try or except executes
    print("Program Executed All The Above Code")

#raising User Defined error in exception handling program does not crash but here it does crash
n = int(input("Enter the number for divider by: "))
if n == 0:
    raise ZeroDivisionError("The Value Zero Cant Be Divided")
else:

    print(12//n)