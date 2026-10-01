data = "hii, this is Roronoa zoro\nAnd Im The Worlds Strongest Swordsmen"

f = open("FileHandling/zoro2.txt","w") #creates the file if not present or opens file for writing
f.write(data)

f.close()#Closing the file

# data = f.readlines()
# print(data) #prints entire data of file as a list element for each lines

# lineData1 = f.readline()  #it will read only a single line untill file returns "" empty string means end of file
# print(lineData1)

# lineData2 = f.readline()
# print(lineData2)