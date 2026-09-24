n = int(input("Enter the number of Lines: "))


#Hollow Cube Pattern
# * * * * * * 
# *         * 
# *         * 
# *         * 
# *         * 
# * * * * * * 

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i == 1 or i == n or j == 1 or j == n):
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     print() 

for i in range(1,n+1):
        if(i == 1 or i == n ):
            print("* "*(n),end="") #for 1st and 2nd row
        else:
            print("* ",end="")#left side
            print("  "*(n-2),end="")#space in middle
            print("* ",end="")#then right side
        print() 