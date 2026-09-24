#Power of Number 
def func(a, b):
    if(b == 0):
        return 1
    else:
        return a*func(a, b-1)   

n = int(input("Enter a Base Number: "))
p = int(input("Enter a Power Number: "))
print(func(n, p))