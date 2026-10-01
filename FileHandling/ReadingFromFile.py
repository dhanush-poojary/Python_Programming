f = open("FileHandling/zoro1.txt")#in python the files will open in read mode

data = f.read()
# r for read, w for write, a for appending to a already exsisting file as w overwrites,rb for open file in binary mode and rt for open file in text mode it is by default mode

#+ for updating
print(data)

f.close()#Close the file

