import random

#takes percentage chance of these being the choice
def chanceOf(one,two,three):
    pass

class GameAI:
    
    def __init__(self,life,ammo,pl,pb):
        self.state=0
        self.life=life
        self.bullets=ammo
        self.lifeGreater=False
        self.changeState(pl,pb)
        
    def action(self):
        newAction=0
        if(self.state==0):
            newAction = 3
        elif(self.state==1):
            newAction = random.choice([1,3])
        elif(self.state==2):
            newAction = random.choice([1,2,3])
        else:
            newAction = random.choice([2,3])

        if(newAction==3):
            self.bullets+=1
        elif(newAction==1):
            self.bullets-=1

        return newAction
    
    def takeHit(self):
        self.life-=1

    def getHp(self):
        return self.life

    def getBullets(self):
        return self.bullets

    #changeState(playerLife,playerBullets)
    def changeState(self,pl,pb):
        if(pl>=self.life):
            self.lifeGreater=False
        else:
            self.lifeGreater=True

        #change from state 0 to other states
        if(self.state==0 and self.bullets>0):
            if(self.lifeGreater):
                self.state=1
            else:
                self.state=2

        #change from state 1 to other states
        if(self.state==1 and self.bullets<1):
            if(pb<1):
                self.state=0
            else:
                self.state=3
        elif(self.state==1 and self.lifeGreater==False):
            self.state=2

        #change from state 2 to other states
        if(self.state==2 and self.bullets<1):
            if(pb<1):
                self.state=0
            else:
                self.state=3
        elif(self.state==2 and self.lifeGreater==True):
            self.state=1

        #change from state 3 to other states
        if(self.state==3 and self.bullets>1):
            if(self.lifeGreater):
                self.state=1
            else:
                self.state=2
        elif(self.state==3 and pb<1):
            self.state=0  
