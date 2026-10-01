def Func():
    print("hello World")

print(__name__)
Func()
#if We Run Main File 
#output --> #__main__
            #hello World

if  __name__ == "__main__":
    print(__name__)
    Func()
    #if We Run Main File within this block
    #output -->#__main__
               #hello World
               #__main__
               #hello World
