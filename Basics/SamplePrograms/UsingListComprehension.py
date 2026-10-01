#using List Comprehension
l1 = [5,4,2,6,4,1]
 
l2 = [ i for i in l1]#i will be stored in l2 in each iterator of for
print(l1)
print(l2)
print("\n")

l2 = [ i+1 for i in l1]#i+1 will be stored in l2 in each iterator of for means element of l1 is made +1 
print(l1)
print(l2)

n = int(input("Enter the Number For Table: "))
l3 = [ n*i for i in range(1,11)]  #stores table n in l3 list

print(l3)

