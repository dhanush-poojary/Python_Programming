# () Tuple is ordered and unchangable ,but can have duplicates it is faster
cars = ("m5","gtr","800","m340i")

print(cars[::])
print(cars[::2])
print(cars[::-1])

print("800" in cars)
print(cars.count("m5"))
print(cars.index("m5"))

for car in cars:
  print(car)
