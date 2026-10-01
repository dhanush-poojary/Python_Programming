from typing import List,Tuple

n : int = 7 #n is typed or named of int data type

def sum(a : int , b : int) -> int :  #is used to name a type to the variable and tells function is writtens int
   return (a+b)

print(sum(10,5))

nums : List[int] = [1,2,3,4,5] #It will mean that all element in the list as int

print(nums, type(nums))#type is list only

tup : Tuple[int] = (1,2,3,4,5)
print(tup, type(tup))