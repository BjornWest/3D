class Observer(object):

    def __init__(self,position,direction,orientation, xFov, yFov):
        self.position = position
        self.direction = direction
        self.orientation = orientation
        self.xFoV = xFov
        self.yFoV = yFov

    def setPos(self, newPos):
        self.Pos = newPos

    def setDirection(self,newDirection):
        self.direction = newDirection

    def setOrientation(self,newOrientation):
        self.orientation = newOrientation