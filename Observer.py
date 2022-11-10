class Observer(object):

    def __init__(self,position,direction,orientation,xFoV,yFoV):
        self.Pos = position
        self.direction = direction
        self.orientation = orientation

    def setPos(self,newPos):
        self.Pos = newPos

    def setDirection(self,newDirection):
        self.direction = newDirection

    def setOrientation(self,newOrientation):
        self.orientation = newOrientation