lis = [1,4,5,8,9,3,6]

def func(x):
    if x%2==0:
        return True
    return False

onlyEven = filter(func,lis)   #The filter function is used to filter elements of list based on function retuned value if true then keep the element if false then return false

print(list(onlyEven))  #filter only return iterable object so we need to boundel it in list