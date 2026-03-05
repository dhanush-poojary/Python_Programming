#Quiz game
questions = ("What is the full form of RAM ?",
             "What is the Name of First programmer ?",
             "How many MegaBytes are there in a GigaByte ?",
             "Is there any faster language then c++ except Assembly ?",
             "Is Computer is a maths machine ?",)
options =(("A. Random Excess Memory","B. Random Memory","C.Read Only Memory","D. Random Access Memory"),
          ("A. Charls babbage","B. guido","C. ichiro oda","D. lady adalovelas"),
          ("A .1Byte","B. 100Byte","C. 1024KByte","D. 1024MByte"),
          ("A .No","B. Python","C. yes","D. Java"),
          ("A .No","B .Yes","C .All of the above","D .None of the above"))

answers = ("D","D","D","A","B")
guess = []
score = 0
question_no = 0

for question in questions:
  print("--------------------------------------------------\n")
  print(f"{question_no+1}. {question}")
  for option in options[question_no]:
    print(f"{option}, ")
  question_no+=1
  guessed = input("Enter your guess(A,B,C,D): ").upper()
  guess.append(guessed)
  if guessed == answers[question_no-1]:
    score+=1
    print("Correct!")
  else:
    print("Incorrect!")
    print(f"{answers[question_no-1]} is the correct answer")


score = (score/len(questions))*100
print("\n\n##############################")
print(f"Your Final Score is {score}")

 