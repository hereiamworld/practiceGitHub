import random

class gameAI:
    
    def __init__(self):
        self.state=0
        self.life=3
        self.bullets=0
        self.lifeGreater=False
        
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

    #changeState(playerLife,playerBullets)
    def changeState(self,pl,pb):
        if(pl>=self.life):
            self.lifeGreater=False
        else:
            self.lifeGreater=True

        #change from state 0 to other states
        if(self.state==0 && self.bullets>0):
            if(self.lifeGreater):
                self.state=1
            else:
                self.state=2

        #change from state 1 to other states
        if(self.state==1 && self.bullets<1):
            if(pb<1):
                self.state=0
            else:
                self.state=3
        elif(self.state==1 && self.lifeGeater==False):
            self.state=2

        #change from state 2 to other states
        if(self.state==2 && self.bullets<1):
            if(pb<1):
                self.state=0
            else:
                self.state=3
        elif(self.state==2 && self.lifeGeater==True):
            self.state=1

        #change from state 3 to other states
        if(self.state==3 && self.bullets>1):
            if(self.lifeGreater):
                self.state=1
            else:
                self.state=2
        elif(self.state==3 && pb<1):
            self.state=0
            
