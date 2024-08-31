# The game() function in a program lets a user play a game and 
# returns the score as an integer. You need to read a file 
# ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. 
# You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.

import random

def game():
    score = random.randint(1,101)
    print("your score is:",score)

    with open("File/score.txt") as f:
        hiscore = f.read()
        if(hiscore == ""):
            hiscore = 0
        else:
            hiscore = int(hiscore)
        
    with open("File/score.txt","w") as f:
        if(score > hiscore or hiscore == 0):
            f.write(str(score))
        else:
            f.write(str(hiscore))
    
game()