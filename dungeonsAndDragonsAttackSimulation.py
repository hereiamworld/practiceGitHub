import time

class Die:
    def __init__(self,numSides):
        self.numSides = numSides

    def roll(self):
        import random
        rng=random.Random()
        return rng.randrange(self.numSides)+1

class D20(Die):
    def __init__(self):
        self.die = Die(20)

    def roll(self,rollType):
        if(rollType in ["A","a"]):
           return self.__rollAdvantage()
        elif(rollType in ["D","d"]):
            return self.__rollDisadvantage()
        else:
            return self.die.roll()
    
    def __rollAdvantage(self):
        rollOne = self.die.roll()
        rollTwo = self.die.roll()
        if(rollOne>rollTwo):
            return rollOne
        else:
            return rollTwo

    def __rollDisadvantage(self):
        rollOne = self.die.roll()
        rollTwo = self.die.roll()
        if(rollOne<rollTwo):
            return rollOne
        else:
            return rollTwo

class Attack:
    def __init__(self,d20,dmgDice,magicMod,abilityMod,proficiencyMod):
        self.d20=d20
        self.dmgDice=dmgDice
        self.magicMod=magicMod
        self.abilityMod=abilityMod
        self.proficiencyMod=proficiencyMod

    def makeAttack(self,rollType):
        return self.d20.roll(rollType) + self.magicMod + self.abilityMod + self.proficiencyMod

    def dealDmg(self):
        return self.dmgDice.roll() + self.magicMod + self.abilityMod

class SaveAttack:
    def __init__(self,ability,saveDC,dmgDice):
        self.ability = ability
        self.saveDC = saveDC
        self.dmgDice = dmgDice

    def getSave(self):
        return self.ability
    
    def checkSave(self,saveNum):
        if (saveNum >= self.saveDC):
            return True 
        else:
            return False

    def dealDmg(self):
        return self.dmgDice.roll()

class Entity:
    def __init__(self,hp,ac,saves,atks,saveAtks):
        self.hp = hp
        self.ac = ac
        self.saves = saves
        self.atks = atks
        self.saveAtks = saveAtks

    def takeDmg(self,damage):
        self.hp -=damage
    
    def makeSave(self,ability,DC,rollType):
        save=D20()
        if(save.roll(rollType) + self.saves[ability] >= DC):
            return False
        else:
            return True

    def checkAtk(self,attack):
        if(attack>self.ac):
            return True
        else:
            return False

    def makeAttack(self,atkNum,rollType,enemy):
        atk = self.atks[atkNum]
        if(enemy.checkAtk(atk.makeAttack(rollType))):
            enemy.takeDmg(atk.dealDmg())

    def forceSave(self,saveNum,enemy):
        save = self.saves[saveNum]
        if(enemy.makeSave(save.ability,save.saveDC,"e")):
            enemy.takeDmg(save.dealDmg())

    def isAlive(self):
        if(self.hp>0):
            return True
        else:
            return False

def fightCommentary(subject, damage) :
    print(f"{subject} attacks!")
    time.sleep(1)
    if(damage > 10):
        print(f"BRUTAL hit for {damage}")
    elif(damage > 0) :
        print(f"Hit for {damage}!")
    else :
        print("Whiff...")
        
secondWindUseLoss=0
secondWindUseWin=0
goblinWins=0
fighterWins=0
for i in range(0,1000000):
    d20=D20()
    sword = Attack(d20,Die(8),0,3,2)
    club  = Attack(d20,Die(8),0,2,2)
    fighter = Entity(13,18,[],[sword],[])
    goblin  = Entity(7,15,[],[club],[])

    fightHp = fighter.hp
    gobHp = goblin.hp
    secondWind = True
    

    while(goblin.isAlive() and fighter.isAlive()):
        ghp = goblin.hp
        fighter.makeAttack(0,"e",goblin)
        fightCommentary("Fighter", (ghp - goblin.hp))
        gobHp -= (ghp - goblin.hp)
        if(gobHp <= 0):
            fighterWins+=1
            print("Killing blow!\nFighter wins!\n\n")
            break
        time.sleep(2)

        fhp = fighter.hp
        goblin.makeAttack(0,"e",fighter)
        fightCommentary("Goblin", (fhp - fighter.hp))
        fightHp -= (fhp - fighter.hp)
        if(fightHp <= 0):
            goblinWins+=1
            print("Killing blow!\nGoblin wins!\n\n")
            break
        time.sleep(2)

        if(fighter.hp<6 and secondWind):
            fighter.takeDmg(-(Die(10).roll()+1))
            #print("Second Wind")
            secondWind=False
            

    if(goblin.isAlive()):
        #print("goblin wins")
        #print ("goblin hp remaining: ",goblin.hp)
        goblinWins+=1
        if(secondWind==False):
            secondWindUseLoss+=1
    else:
        #print("fighter wins")
        #print ("fighter hp remaining: ",fighter.hp)
        fighterWins+=1
        if(secondWind==False):
            secondWindUseWin+=1

print("")
print("")
print("Fighter wins: ",fighterWins)
print("        secondWindUses",secondWindUseWin)
print("Goblin wins: ",goblinWins)
print("        secondWindUses",secondWindUseLoss)
