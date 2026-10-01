#Exception means run time errors
def main():
    try:
        n = int(input("Enter the number for divider by: "))
        print(12//n)
        return
    except ZeroDivisionError:
        print("Division by Zero")
        return
    finally:
        #it will executes either try or except executes but it's main purpose is within a function after returning from try or except block ,if we need any code 
        print("hey This is Finally That is executed even after returning a function")
    
   #print("hey This is End Of Function")

main()