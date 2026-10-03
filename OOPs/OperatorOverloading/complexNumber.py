class complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i

    def __add__(self, c2):
        return complex(self.r + c2.r, self.i + c2.i)

    def __mul__(self, c2):
            return complex((self.r * c2.r -  self.i * c2.i) ,(self.r * c2.i -  self.i * c2.r) )
    
    def __str__(self):
        return f"{self.r} + {self.i}i"
c1 = complex(2,3)
c2 = complex(5,2)
print(c1 + c2) #<__main__.complex object at 0x0000018305F7CB90> before __str__ decorator

print(c1 * c2)


#print the length of a list
#print(len([1,2,3])) before Dunder Function means error
def __len__(n):
     return len(n)

print(len([1,2,3]))

