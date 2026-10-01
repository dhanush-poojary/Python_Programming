with open ("FileHandling/zoro3.txt","w") as f:#inside the folder FileHand.. bcz pwd is python_programming
    f.write("Hii this is Charizard!!!")
    #as file is open in write mode we can not read the data from that now  open it again in read mode
with open("FileHandling/zoro3.txt") as f:
    data = f.readlines()
    print(data)

#when using with statement we dont need to close the file manually it is done automatically
