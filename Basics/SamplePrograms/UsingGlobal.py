a = 69

def func():
    global a #It will refer to global variable rather then create a local scope variable
    a = 3
    print(a)

print(a)
func()
print(a)