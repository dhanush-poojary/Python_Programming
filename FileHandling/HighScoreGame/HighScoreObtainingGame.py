#High Score Obtaining Game, Who Gets Highest Will Win The Game
import random                      #High Score will be stored in file
         
def Game():
   print("Who Gets Maximum High Score Wins!!!\n")
   score = random.randint(1,999) #random integer from 1 to 999

   if(score == 999):
       print("Congratulations You Won The By Highest Score {9999}")
   else: 
        print(f"Your Score {score}")

   with open("FileHandling/HighScoreGame/Hiscore.txt") as f: #Open file for reading previous high score
      hiscore = f.read()

      if(hiscore != ""): #if previous highscore is not there or not yet made
            hiscore = int(hiscore)
      else:
          hiscore = 0
   if(score>hiscore): #only if present score is > then previous score
        print(f"You Won!!!, The High Score Was {hiscore}\n")

        with open("FileHandling/HighScoreGame//Hiscore.txt","w") as f:   #it will overwrite the previous high score
            f.write(str(score))#new high score to file
        
   else:
       print(f"You Loose <3,The High Score was {hiscore}\n")

Game()