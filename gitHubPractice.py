#import gameAI
#3/2/2018
#Alexander & Alexandre
#Shoot, Sheild, Reload
 

#Cheats
space2 ="_________________________________________________________________________"
space = "-------------------------------------------------------------------------" 
#Intro
print(space2)
print("\t\tSHOOT SHEILD RELOAD by Alexes")
print(space)

print("\n\t\tThe rules of the game:")
print("  Shoot other person without them sheilding and Win! ")
print(space2) 

#Names
print(space2) 
print("\t\t\tPLAYERS") 
print(space) 
myName = input("\n\t\tEnter in your name: ")
enemyName = input("\t\tEnter in Enemy name: ")
print("\n\tOk " + myName + ", you will be dueling against "+enemyName+"!")
print(space2) 
#Difficulty
print(space2)
print("\t\t\tDIFFICULTY")
print(space)
answer = 0
while(answer == 0):
    difficultyNum = input("\n\t\t\t1 = easy\n\t\t\t2 = medium\n\t\t\t3 = hard\n\n\t\tSelect "+enemyName+"'s Difficulty: ")
    answer = 1
    if(difficultyNum == "1"):
        difficulty = "EASY"
    elif(difficultyNum == "2"):
        difficulty = "MEDIUM"
    elif(difficultyNum == "3"):
        difficulty = "HARD"
    else:
        answer = 0
        print("\n\t!!!!!Invalid answer, please try again!!!!!\n"+space)
print("\n\t\tYou have selected: \""+difficulty+"\"")

#Human/Computer variables
if difficulty == "EASY":
    Hammo   = 0
    Hsheild = 10
    Hshoot  = 0
    Hlife   = 10
    Cammo   = 0
    Csheild = 10
    Cshoot  = 0
    Clife   = 3
elif difficulty == "MEDIUM":
    Hammo   = 0
    Hsheild = 6
    Hshoot  = 0
    Hlife   = 6
    Cammo   = 0
    Csheild = 10
    Cshoot  = 0
    Clife   = 6
else:
    Hammo   = 0
    Hsheild = 3
    Hshoot  = 0
    Hlife   = 3
    Cammo   = 9999
    Csheild = 9999
    Cshoot  = 0
    Clife   = 10

#other variables
roundNum = 0
#Gameplay
#while(Hlife & Clife > 0):
while (roundNum < 10):
    print(space2) 
    roundNum += 1
    print("|\t\t\t\tRound", roundNum,"\t\t\t\t|")
    print(space)    
    print("|\t",myName,"\t\t|\tACTIONS\t\t|\t ", enemyName,"\t|")
    print(space)
    print("|\tAmmo   = ",Hammo,"\t|\t1 = Shoot\t|\tAmmo   = ",Cammo,"\t|")
    print("|\tSheild = ",Hsheild,"\t|\t2 = Sheild\t|\tSheild = ",Csheild,"\t|")
    print("|\tHealth = ",Hlife,"\t|\t3 = Reload\t|\tHealth = ",Clife,"\t|")
    print("|\t\t\t\t\t\t\t\t\t|")
#    if you shoot
#HUMAN ACTIONS
    print(space2)
    while(answer == 1):
        actionNum = input("\n\t\t\t     Enter action: ")
        answer = 0
        if(actionNum == "1"):
            action = "SHOOT"
        elif(actionNum == "2"):
            action = "SHEILD"
        elif(actionNum == "3"):
            action = "RELOAD"
        else:
           answer = 1
           print("\n\t!!!!!Invalid answer, please try again!!!!!\n"+space)
    answer = 1

#COMPUTER ACTIONS  
    if roundNum == 1:
        Caction = 1
    else:
        Caction = 2
    print (Caction)
#END    
if Hlife ==0 and Clife == 0:
    print("YOU TIED!")
elif Clife == 0:
    print("YOU WIN!")
elif Hlife == 0:
    print("YOU LOSE!")

    
ammo = 0
sheild = 0