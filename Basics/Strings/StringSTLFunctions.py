name = "zoro"

print(len(name))

print(name.endswith("ro"))#returns true or false based o Substring is present or not
print(name.startswith("zo"))
print(name.capitalize())#only first word of string is capitalized

print("\\")#prints '\'
print("\;")#prints ';'

words = '''hey this is |name|    #Multiline String
and he is the 
Greatest |Power| in the world'''

print(words.replace("|name|", name).replace("|Power|", "Swordsmen")) 

print("hii\n"*3)#string will be printed multiple times
#for this the time complexity for worst case will be O(N)