class car:
    model  = None
    def __init__(self,model,horsePower):
        self.model  = model
        super().__init__(horsePower)
    def show(self):
        print(f"The model is : {self.model}")

class sports:
    horsePower = None
    def __init__(self,horsePower):
        self.horsePower  = horsePower
    def show(self):
          print(f"The model is : {self.horsePower}") 
    
class bmw(car,sports):
    name = "bmw"
    def __init__(self,model,horsePower):
        super().__init__(model,horsePower)
      
   

b = bmw(1997,600)

print(b.name)
print(b.horsePower)
print(b.model)

