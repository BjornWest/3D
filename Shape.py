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
                    if self.coords[x][y][z] == True:
                        v += 1
        return v



radius = 50
l1 = [False for x in range(radius*2)]
l2 = [l1 for x in range(radius*2)]
cubeCoords = [l2 for x in range(radius*2)]



count = 0
for x in range (radius*2):
    for y in range(radius*2):
        for z in range(radius*2):
            if math.sqrt((x-radius)**2 + (y-radius)**2 + (z-radius)**2)<radius:
                cubeCoords[x][y][z] = True
                count += 1

cubeRGB = (0,100,0)
        
cube = Shape(cubeCoords,cubeRGB)

a = cube.getVolume()
print("V= ",a)
print(count)






