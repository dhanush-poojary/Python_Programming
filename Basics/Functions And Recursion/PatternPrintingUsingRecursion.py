num = int(input("Enter a number of lines: "))
def pattern(n = 0):
    if(n == num ):
        return
    print("*" * n)  #instead of loop we used string repeatation but same time complexity
    pattern(n+1)

pattern()
