class Number:
    def __init__(self,n):
        self.n = n

    def __add__(self, num):
       return self.n + num.n

print(1+3)
n = Number(2)
m = Number(1)
print(m+n)