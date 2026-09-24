p1 = "subscribe" #spam words
p2 = "buy course"

message = input("Enter your comment: ") #hello everyone subscribe to my channel 

if((p1 in message) or (p2 in message)):#in is used to check whether str1 is a substring of str2
    print("yes This comment is a spam")
else:
    print("No This comment is not a spam")