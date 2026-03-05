# Dictionary is a collection of {key:value} pairs ordered and chagable ,No duplicates

dic = {"Cricket":"Dhoni","FootBall":"Ronaldo","F1":"Max verstappen"}
print(dic)

# key = dic.keys()
# print(key)
# for key in dic.keys():
#   print(key,end=" ")
# print()

# val = dic.values()
# print(val)
# for val in dic.values():
#   print(val,end=" ")
# print()



print(dic.get("bgmi"))#key not present
print(dic.get("Dhoni"))#present but not as a key but as a value
print(dic.get("Cricket"))

dic.update({"F1":"Formula 1"})
print(dic.get("F1")) 

dic.pop("Cricket")
print(dic.get("Cricket"))
dic.popitem()#it will only remove a last value which is inserted

print(dic)

item = dic.items()
print(item)#it will return key,value in a 2D list of tuples
for key,value in dic.items():
  print(f"{key}:{value}")


