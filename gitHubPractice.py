from gameAI import GameAI
from random import *
#3/2/2018
#Alexander & Alexandre
#Shoot, shield, Reload
 

#Cheats
space = "-------------------------------------------------------------------------"
space2 = "_________________________________________________________________________"
space3 = "|-----------------------------------------------------------------------|" 
#Intro
print(space2)
print("\t\tSHOOT SHIELD RELOAD by Alexes")
print(space)

print("\n\t\tThe rules of the game:")
print("  Shoot other person without them shielding and Win! ")
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
    Hshield = 10
    Hshoot  = 0
    Hlife   = 12
    Cammo   = 0
    Cshield = '∞'
    Cshoot  = 0
    Clife   = 5
elif difficulty == "MEDIUM":
    Hammo   = 0
    Hshield = 9
    Hshoot  = 0
    Hlife   = 3
    Cammo   = 1
    Cshield = '∞'
    Cshoot  = 0
    Clife   = 3
else:
    Hammo   = 0
    Hshield = 6
    Hshoot  = 0
    Hlife   = 3
    Cammo   = 2
    Cshield = '∞'
    Cshoot  = 0
    Clife   = 4
    
gameai = GameAI(Clife,Cammo,Hlife,Hammo)


#other variables
roundNum = 0
#Gameplay
while (Hlife and gameai.getHp() > 0):
    print(space2) 
    roundNum += 1
    print("|\t\t\t\tRound", roundNum,"\t\t\t\t|")
    print(space3)    
    print("|\t",myName,"\t\t|\tACTIONS\t\t|\t ", enemyName,"\t|")
    print(space3)
    print("|\tAmmo   = ",Hammo,"\t|\t1 = Shoot\t|\tAmmo   = ",gameai.getBullets(),"\t|")
    print("|\tShield = ",Hshield,"\t|\t2 = Shield\t|\tShield = ",Cshield,"\t|")
    print("|\tHealth = ",Hlife,"\t|\t3 = Reload\t|\tHealth = ",gameai.getHp(),"\t|")
    print(space3)

#HUMAN ACTIONS
    answer = 1
    while(answer == 1):
        actionStr = input("\n\t\t\t     Enter action: ")
        if(actionStr.isdigit()):
            actionNum= int(actionStr)
        else:
            actionNum= 0
        answer = 0
        if(actionNum != 1 and  actionNum != 2 and actionNum != 3):
           answer = 1
           print("\n\t!!!!!Invalid answer, please try again!!!!!\n"+space)
        if (actionNum == 1 and Hammo == 0):
            answer = 1
            print("\n\t!!!!!No Ammo, please try again!!!!!\n"+space)
        if (actionNum ==2 and Hshield == 0):
            answer = 1
            print("\n\t!!!!!No Shield, choose a different option!!!!!\n"+space)

#COMPUTER ACTIONS  
    Caction = gameai.action()   

#Both Actions(Results)
    result = actionNum*10 + Caction 

    if result == 11:
        Hammo -= 1
        Hlife -= 1
        gameai.takeHit()
        print("\t\t\tBoth of ya'll got shot!")
    elif result == 12:
        Hammo -= 1
        print("\t\t\t"+enemyName+" deflected the bullet")
    elif result == 13:
        Hammo -= 1
        gameai.takeHit()
        print("\t\t\tYou shot "+ enemyName+ " as he reloaded")
    elif result == 21:
        Hshield-=1
        print("\t\t\tYou deflected the bullet") 
    elif result == 22:
        Hshield-=1
        print("\t\t\tBoth of ya'll shielded")
    elif result ==23:
        Hshield-=1
        print("\t\t\t"+enemyName +" reloaded as you shielded")
    elif result ==31:
        Hammo +=1
        Hlife -= 1
        print("\t\t\t"+enemyName+" shot you as you reloaded")
    elif result == 32:
        Hammo += 1
        print("\t\t\tYou reloaded as "+enemyName+" shielded")
    elif result == 33:
        print("\t\t\tYa'll both reloaded")
        Hammo += 1
    else:
        print("\t\t\twtf did you do to break this?")
    gameai.changeState(Hlife,Hammo)
#END    
if Hlife ==0 and gameai.getHp() == 0:
    print(space2) 
    print("|\t\t\tYa'll Killed each other\t\t\t\t|")
    print("|\t\t\t\tTIE!!!!\t\t\t\t\t|")
    print(space3) 
elif (gameai.getHp() == 0):
    print(space2) 
    print("|\t\t\t\tYou killed "+enemyName+"!\t\t\t|")
    print("|\t\t\t\tYOU WIN!!!!\t\t\t\t|")
    print(space3)
elif Hlife == 0:
    print(space2) 
    print("|\t\t\t\t"+enemyName+" killed you!\t\t\t|")
    print("|\t\t\t\tYOU LOSE!!!!\t\t\t\t|")
    print(space3)
