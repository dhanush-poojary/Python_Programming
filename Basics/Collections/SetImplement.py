# {} set is unordered and immutable and no duplicates ,but can add or remove elements
nums = {1,33,45,2,52,56,22}

for i in nums:
   print(f"{i} ",end="")

print(52 in nums)#find a element

nums.add(66)
for i in nums:
   print(f"{i} ",end="")
print()
nums.pop()#deletes a random element   
for i in nums:
   print(f"{i} ",end="")