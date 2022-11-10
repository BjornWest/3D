import math
class Shape(object):
    #coords is a bool triple array designating which coordinates the shape occupies
    #rgb is the color [x,y,z] of the shape where x, y and z range from 0 to 255
    def __init__(self,coords,rgb):
        self.coords = coords
        self.rgb = rgb
        self.getSpace = len(coords)*len(coords[0])*len(coords[0][0])
        

    def getVolume(self):
        v = 0
        for x in range(len(self.coords)):
            for y in range(len(self.coords[0])):
                for z in range(len(self.coords[0][0])):
                    if self.coords[x][y][z]:
                        v += 1
        return v






# creating a globe


def globe(radius):
    cubeCoords = []
    for x in range (radius*2):
        cubeCoords.append([])
        for y in range(radius*2):
            cubeCoords[x].append([])
            for z in range(radius*2):
                if math.sqrt((x-radius)**2 + (y-radius)**2 + (z-radius)**2)<radius:
                    cubeCoords[x][y].append(True)
                else:
                    cubeCoords[x][y].append(False)
    return cubeCoords





