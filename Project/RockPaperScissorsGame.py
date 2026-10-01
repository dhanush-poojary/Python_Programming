import random
import pyttsx3

engine = pyttsx3.init("sapi5")

engine.say("Welcome to Rock Paper Scissors Game")

engine.say("Enter the number of rounds")
engine.runAndWait()

n = int(input("Enter the number of rounds: "))

lis = ["rock", "paper", "scissors"]

choiceCount = 0
oponentCount = 0

while n:

    engine.say("Rock Paper Scissors")

    print("Rock\tPaper\tScissors\n")

    engine.say("Enter your choice")
    engine.runAndWait()

    choice = input("Enter your Choice: ").lower()

    print(f"Your Choice: {choice}")

    n -= 1

    OponentChoice = random.choice(lis)

    print(f"Opponent Choice: {OponentChoice}\n")


    if choice == "rock" and OponentChoice == "paper":
        print("Computer Won!!")
        oponentCount += 1

    elif choice == "paper" and OponentChoice == "scissors":
        print("Computer Won!!")
        oponentCount += 1

    elif choice == "scissors" and OponentChoice == "rock":
        print("Computer Won!!")
        oponentCount += 1

    elif choice == "rock" and OponentChoice == "scissors":
        print("You Won!!")

        choiceCount += 1

    elif choice == "paper" and OponentChoice == "rock":
        print("You Won!!")
        choiceCount += 1

    elif choice == "scissors" and OponentChoice == "paper":
        print("You Won!!")
        choiceCount += 1

    else:
        print("Match Drawn")

    print()


if choiceCount > oponentCount:
    print("You Won!!")
elif choiceCount == oponentCount:
    print("Match Drawn")
    
else:
    print("Computer Won!!")
  

