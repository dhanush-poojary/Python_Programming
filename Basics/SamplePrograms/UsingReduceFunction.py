from functools import reduce

lis = [1,2,3,4,5]
sum = lambda x,y : x+y

print(reduce(sum,lis)) #The reduce function will call sum function for each element of list
#it will take pair and apply sum function and then result of pair with next element and so on

#sum(1,2)->3
#sum(3,3)->6
#sum(6,4)->10
#sum(10,5)->15

mul = lambda x,y : x*y
#mul(1,2)->2
#mul(2,3)->6
#mul(6,4)->24
#mul(24,5)->120
print(reduce(mul,lis))