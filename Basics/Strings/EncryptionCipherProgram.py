#Encryption cipher program  And Decryption
import  random
import string

chars  = " "+string.punctuation+string.digits+string.ascii_letters
         #space #symbols               #digits       #alphabets

pattern = list(chars)#all in list

key = pattern.copy()

random.shuffle(key)#randomly shuffling elements of key list

plainText = input("Enter the text To Encrypt: ") #plaintext to encrypt

cipherText = ""

for str in plainText:   #Encrypting
     idx = chars.index(str)    #index of plaintext's current character in chars list
     cipherText+=(key[idx])    #finding the corresponding or random element in that index in key list

print(f"\nPlainText: {plainText}")
print(f"CipherText: {cipherText}\n")

plainText = "" 
for str in cipherText:   #Decryption
     idx = key.index(str)    #index of Ciphertext's current character in keys list
     plainText+=(pattern[idx])#finding the corresponding element in that index in pattern list

print(f"Original PlainText: {plainText}")

