class Employee:
    Name = "DJ Bravo"#Acts as a default value for all objects
    Id  =  999

     #here self can be any other variable name it is needed bcz of instance
    def __init__(self): #Dunder function a function with __and__ , it is a constructor
        print("Object is Created")

    def getInfo(self):
        print(f"Name: {self.Name} , and Id: {self.Id}")

    @staticmethod  #it is a decorator which is written with @
    def printInfo():#in this function we dont need any class attributes or self instance so we crated it with as a static mathod
        print("Hello Employees")

emp = Employee()

print(f"Name: {emp.Name} , and Id: {emp.Id}")

emp.getInfo()
#emp.getInfo(emp) #Instead of doing this just put a self and no need to pass emp or any instance


emp.Name = "Dhoni"
emp.Id = 7

print(f"Name: {emp.Name} , and Id: {emp.Id}")

emp.printInfo()

emp.salary = 1000  #Instance Attribute not a class Attribute

print("Salary: ",emp.salary)

