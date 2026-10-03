#program to Convert Full Name to First And Second Name Based on Space (Abstraction)
class Emp:

    @property
    def name(self):
        return self.fname+self.sname

    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0] #after split we get list of 2 ele then insert 0 to fname
        self.sname = value.split(" ")[1] #after split we get list of 2 ele then insert 1 to sname

a = Emp
#print(a.name) #Error not valid
a.name = "Roronoa Zoro"
print(a.name)

#print(a.fname,a.sname)
    