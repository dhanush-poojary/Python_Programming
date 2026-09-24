tup = (1,)
print(type(tup))
tup = (1)
print(type(tup))

t = (3,2,3,4,3)
num = t[2:5].index(3)#finds index of 3 between the range 2 to 5
print(num)


name = "Zoro"
age = 21

person = name, age #tuple Packing

print(person)