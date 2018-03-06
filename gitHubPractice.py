#import gameAI
from random import *
#3/2/2018
#Alexander & Alexandre
#Shoot, Sheild, Reload
 

#Cheats
space = "-------------------------------------------------------------------------"
space2 = "_________________________________________________________________________"
space3 = "|-----------------------------------------------------------------------|" 
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
    Hsheild = '∞'
    Hshoot  = 0
    Hlife   = 10
    Cammo   = 0
    Csheild = '∞'
    Cshoot  = 0
    Clife   = 5
elif difficulty == "MEDIUM":
    Hammo   = 0
    Hsheild = '∞'
    Hshoot  = 0
    Hlife   = 3
    Cammo   = 0
    Csheild = '∞'
    Cshoot  = 0
    Clife   = 3
else:
    Hammo   = 0
    Hsheild = '∞'
    Hshoot  = 0
    Hlife   = 5
    Cammo   = 10
    Csheild = '∞'
    Cshoot  = 0
    Clife   = 10

#other variables
roundNum = 0
#Gameplay
while (Hlife and Clife > 0):
    print(space2) 
    roundNum += 1
    print("|\t\t\t\tRound", roundNum,"\t\t\t\t|")
    print(space3)    
    print("|\t",myName,"\t\t|\tACTIONS\t\t|\t ", enemyName,"\t|")
    print(space3)
    print("|\tAmmo   = ",Hammo,"\t|\t1 = Shoot\t|\tAmmo   = ",Cammo,"\t|")
    print("|\tSheild = ",Hsheild,"\t|\t2 = Sheild\t|\tSheild = ",Csheild,"\t|")
    print("|\tHealth = ",Hlife,"\t|\t3 = Reload\t|\tHealth = ",Clife,"\t|")
    print(space3)

#HUMAN ACTIONS
    answer = 1
    while(answer == 1):
        actionNum = int(input("\n\t\t\t     Enter action: "))
        answer = 0
        if(actionNum != 1 and  actionNum != 2 and actionNum != 3):
           answer = 1
           print("\n\t!!!!!Invalid answer, please try again!!!!!\n"+space)
        if (actionNum == 1 and Hammo == 0):
            answer = 1
            print("\n\t!!!!!No Ammo, please try again!!!!!\n"+space)    

#COMPUTER ACTIONS  
    if roundNum == 1:
        Caction = 3
    elif Cammo != 0:
        Caction = randint(1,3)
    else:
        Caction = randint(2,3)    

#Both Actions(Results)
    result = actionNum*10 + Caction 

    if result == 11:
        Hammo -= 1
        Cammo -= 1
        Hlife -= 1
        Clife -= 1
        print("\t\t\tBoth of ya'll got shot!")
    elif result == 12:
        Hammo -= 1
        print("\t\t\t"+enemyName+" deflected the bullet")
    elif result == 13:
        Hammo -= 1
        Cammo += 1
        Clife -= 1
        print("\t\t\tYou shot "+ enemyName)
    elif result == 21:
        Cammo -=1
        print("\t\t\tYou deflected the bullet") 
    elif result == 22:
        print("\t\t\tBoth of ya'll sheilded")
    elif result ==23:
        Cammo += 1
        print("\t\t\t"+enemyName +" reloaded as you sheilded")
    elif result ==31:
        Hammo +=1
        Cammo -= 1
        Hlife -= 1
        print("\t\t\t"+enemyName+" shot you as you reloaded")
    elif result == 32:
        Hammo += 1
        print("\t\t\tYou reloaded as "+enemyName+" sheilded")
    elif result == 33:
        print("\t\t\tYa'll both reloaded")
        Hammo += 1
        Cammo += 1
    else:
        print("\t\t\twtf did you do to break this?")                                   
#END    
if Hlife ==0 and Clife == 0:
    print(space2) 
    print("|\t\t\tYa'll Killed each other\t\t\t\t|")
    print("|\t\t\t\tTIE!!!!\t\t\t\t\t|")
    print(space3) 
elif Clife == 0:
    print(space2) 
    print("|\t\t\t\tYou killed "+enemyName+"!\t\t\t|")
    print("|\t\t\t\tYOU WIN!!!!\t\t\t\t|")
    print(space3)
elif Hlife == 0:
    print(space2) 
    print("|\t\t\t\t"+enemyName+" killed you!\t\t\t|")
    print("|\t\t\t\tYOU LOSE!!!!\t\t\t\t|")
    print(space3)

    
ammo = 0
sheild = 0