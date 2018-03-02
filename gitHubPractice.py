#3/2/2018
#Alexander & Alexandre
#Shoot, Sheild, Reload


#Intro
print("Hello and Welcome to the first game made by both Alexandre and Alexander")
print("\n\t\tThe rules of the game:")
print("  Shoot other person without them sheilding and Win! ")
print("\n\t\t\tOptions:")
print("\t\t  Shoot--Sheild--Reload")

#Names
myName = input("\n\nEnter in your name: ")
enemyName = input("\n\nEnter in Enemy name: ")
print("\nOk " + myName + ", you will be dueling against "+enemyName+"!\n")

#Difficulty
answer = 0
while(answer == 0):
    print("What difficulty do you want "+enemyName+" to be on?\n")
    difficultyNum = input("\t1 = easy\n\t2 = medium\n\t3 = hard\n")
    answer = 1
    if(difficultyNum == "1"):
        difficulty = "EASY"
    elif(difficultyNum == "2"):
        difficulty = "MEDIUM"
    elif(difficultyNum == "3"):
        difficulty = "HARD"
    else:
        answer = 0
        print("That was an invalid answer, please try again")
print("\nYou have selected: \""+difficulty+" MODE\"")

#Human/Computer variables
if(difficulty == "EASY"):
    Hammo   = 0;
    Hsheild = 10;
    Hshoot  = 0;
    Hlife   = 10;
    Cammo   = 0;
    Csheild = 10;
    Cshoot  = 0;
    Clife   = 3;
elif(difficulty == "MEDIUM"):
    Hammo   = 0;
    Hsheild = 6;
    Hshoot  = 0;
    Hlife   = 6;
    Cammo   = 0;
    Csheild = 10;
    Cshoot  = 0;
    Clife   = 6;
else:
    Hammo   = 0;
    Hsheild = 3;
    Hshoot  = 0;
    Hlife   = 3;
    Cammo   = 9999;
    Csheild = 9999;
    Cshoot  = 0;
    Clife   = 10;

#other variables
roundNum = 0
#Gameplay
while(Hlife & Clife > 0):
    roundNum += 1
    print("Round "+roundNum+"!\n")


