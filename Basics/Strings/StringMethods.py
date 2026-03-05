print(help(str))#prints description of various string methods

name = "RoRonoa Zoro"

result1 = name.find("a")#it follows 0 based indexing
result2 = name.rfind("o")#it finds character from the back

print(result1)
print(result2)

name = "zoro"
print(name.capitalize())#first letter after space will be capitalized
print(name.upper())#all letters of string

name = "RoRonoa Zoro"

result = name.count("o")
print(result)


Dob = input("Enter dob: ")
Dob = Dob.replace("-","/")

print(Dob)
