#User name Validation 
User_Name = input("Enter The User Name: ")

if(len(User_Name) <= 12):
 if(not User_Name.count(" ")):
   if(User_Name.isalpha()):
      print(f"User Name {User_Name} is Valid")
   else:
     print("It contains Digits!!")
 else:
     print("it contains Spaces!!")
else:
   print("it's Length is more then 12")
    