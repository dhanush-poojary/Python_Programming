# [] lits are ordered and changable can have duplicates
cars = ["m5","gtr","800","m340i"]

print(cars[::])
print(cars[::2])
print(cars[::-1])

for car in cars:
  print(car)

cars.append("supra")

print(cars[::])
cars.insert(2,"maruthi 800")
print(cars[::])

nums = [4,56,3,5,2,1]
nums.sort()
print(nums[::])
nums.reverse()
print(nums[::])

print(nums.index(56))
print(nums.count(2))