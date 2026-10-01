import random

num = random.randint(1,100)
n = 0
Guesses = 1

print("_________________Guess Perfect Number in Minimum Attempt_________________________")


while num != n:

    n = int(input("Enter your Guess: "))
    
    if n < num:
        print("The number is higher")
       
    elif n > num:
        print("The number is lower")
      
    if(num == n):
        break
    Guesses+=1


print("_______________________________________")
print(f"You Guessed the number {num} after {Guesses} Attempts")
with open("Project/PerfectNumberGuess/Hiscore.txt") as f:
      hiscore = f.read()
      if(hiscore != ""):
            hiscore = int(hiscore)
      else:
          hiscore = 100
if(Guesses<=hiscore):
        print(f"You Won!!!, The Previous Lowest Score Was {hiscore}\n")
        with open("Project/PerfectNumberGuess/Hiscore.txt","w") as f:
            f.write(str(Guesses))
else:
      print(f"The Previous Lowest Score Was {hiscore}\n")       