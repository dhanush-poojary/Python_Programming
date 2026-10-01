#creating Multiple files in 1 with statement
with (
    open("FileHandling/MultipleFiles/test1.txt", "w") as f1,  
    open("FileHandling/MultipleFiles/test2.txt", "w") as f2
):
    f1.write("Hii, Im Writting this in Test file 1")
    f2.write("Hii, Im Writting this in Test file 2")