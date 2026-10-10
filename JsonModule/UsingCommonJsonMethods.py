import json
#JSON (JavaScript Object Notation) is a lightweight data format used for data exchange between servers and applications. It is widely used in APIs, web applications, and configurations.

py_obj = {"Name" : "Zoro","Age":19,"Work":"Hunter"} #python object or dictionary
print(py_obj)#prints normal dictionary
print(type(py_obj))
js_obj = json.dumps(py_obj) #it will convert python object into json string
print(js_obj)#prints json string
print(type(js_obj))#prints str as it is json string not a python dictionary or object


py_obj = json.loads(js_obj)#it will convert the json string back into a python string
print(py_obj)#prints dictionary
print(type(py_obj))

print("\nFormatting dumped string")


obj_py = {"Name" : "luffy","Age":20,"Work":"Pirate King"}
print(obj_py,type(obj_py))

obj_js = json.dumps(obj_py,indent=4)
print(obj_js,type(obj_js))