n = int(input("Enter the number of lines: "))

#Star pyramid Pattern
#    *
#   ***
#  *****
# *******

nst = 1
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    # for j in range(nst):
    #     print("*",end="")
    # nst += 2
    for j in range(1,2*i):#2*i-1 is a method to print odd number series
        print("*",end="")
    print()

# for i in range(1,n+1):
#     print("*"*i,end="")
#     print()