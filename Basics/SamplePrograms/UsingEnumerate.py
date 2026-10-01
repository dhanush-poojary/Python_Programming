#using Enumarate in for loop instead of range
l = [5,4,2,6,4,1]

print("Index\tItem")
for idx,itm in enumerate(l):  #it is same as dictionary's dic.items()
    #enumarate will give index and key/value of elemenets present in list in each iteration
    print(f"{idx}   ->   {itm}")