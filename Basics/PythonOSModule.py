import os

path = "G:\Code Base" #directory to search
contents = os.listdir(path)#it will provide a list of names of files present in directory

for item in contents:#iterating through each element
    print(item)