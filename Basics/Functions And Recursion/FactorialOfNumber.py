#Prints the factorial of n 
def func(n):
    if(n == 0 or n == 1): #0 and 1's factorial is 1
        return 1
    else:
        return n*func(n-1) 

n = int(input("Enter a number: "))
result = func(n)
print(f"Factorial of {n} is {result}")
