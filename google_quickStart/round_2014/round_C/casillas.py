
class Casillas:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.state = True
        self.type = 1

    
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getType(self):
        return self.type

    def setType(self,ty):
        self.type = ty

    def getState(self):
        return state
    
    def setEstado(self,state):
        self.state = state

    def toString(self):
        return("(%r,%r)" %(self.x,self.y))