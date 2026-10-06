#Map Function is used when we want to run the function for each element present in the list
lis = [1,2,3,4,5]

sqrt = lambda x : x*x

sqrt_lis = map(sqrt,lis) #it will execute sqrt function for all elements of list

print(list(sqrt_lis)) #Map only return iterable object so we need to boundel it in list

def func(x : int) -> int:
    return x*x

_list = map(func,lis)
print(list(_list))  #Map only return iterable object so we need to boundel it in list

