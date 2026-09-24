a = {}#Creates an empty disctionary

a = set()#Creates an empty set

a.add(1)
a.add(2)
a.add(3)
a.add(4)
print(a)
a.pop()#deletes a random element
print(a)
a.remove(2)#deletes a specific element
print(a)

a.clear()#empty the set


#Set union and Intersection
a = {1,2,3,4,5}
b = {4,5,6,7,8}
c = a.union(b) #bascically joins bothe  sets together
print(c)
d = a.intersection(b)#basically returns common element in both sets
print(d)


