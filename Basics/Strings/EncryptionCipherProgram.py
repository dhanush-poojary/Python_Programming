import  random
import string

chars  = " "+string.punctuation+string.digits+string.ascii_letters

pattern = list(chars)

key = pattern.copy()

random.shuffle(key)

plainText = input("Enter the text To Encrypt: ")

cipherText = ""

for str in plainText:
     idx = chars.index(str)
     cipherText+=(key[idx])

print(f"\nPlainText: {plainText}")
print(f"CipherText: {cipherText}\n")

plainText = ""
for str in cipherText:
     idx = key.index(str)
     plainText+=(pattern[idx])

print(f"Original PlainText: {plainText}")

