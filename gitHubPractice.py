import gameAI
#3/2/2018
#Alexander & Alexandre
#Shoot, Sheild, Reload

#variables
answer = 0

#Intro
print("Hello and Welcome to the first game made by both Alexandre and Alexander")
print("\n\t\tThe rules of the game:")
print("  Shoot other person 3 times without them sheilding and Win! ")
print("\n\t\t\tOptions:")
print("\t\t  Shoot--Sheild--Reload")

#Name
name = input("\n\nEnter in your name: ")

#Difficulty
while(answer == 0):
    print("\nOk " + name + ", Pick your difficulty:")
    difficultyNum = input("\t1 = easy\n\t2 = medium\n\t3 = hard\n")
    answer = 1
    if(difficultyNum == 1):
        difficulty = "EASY"
    elif(difficultyNum == 2):
        difficulty = "MEDIUM"
    elif(difficultyNum == 3):
        difficulty = "HARD"
    else:
        answer = 0
        print("That was an invalid answer, please try again")
print("\nYou have selected: \""+difficulty+" MODE\"")

    

ammo = 0
sheild = 0

