#email slicer program
email = input("Enter your Email: ")

index = email.index("@")

userName = email[:index]
domain = email[index+1:]

print(f"UserName : {userName} and Domain : {domain}")