import json

py_obj = {"Name" : "Zoro","Age":19,"Work":"Pirate"} #python object or dictionary

with open("JsonModule/data.json","w") as f:
    json.dump(py_obj,f) #it will insert or dump python object or string or dictionary into a json file
    #json.dump(py_obj,f,indent=4)#it will format the string into different lines

with open("JsonModule/data.json") as f:
    obj = json.load(f)#it will extract dumped python object or string or it will extract json file data and convert it as a dictionary/string
print(obj)
print(type(obj))
