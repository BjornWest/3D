import math


class Shape(object):
    # position is the position of the center of the total rectangle
    # coords is a bool triple list designating which coordinates the shape occupies
    # rgb is the color [x,y,z] of the shape where x, y and z range from 0 to 255
    # orienation consists of 4 values, the first 3 describing a vector and the 4th the rotation around that vector in degrees
    # standard orientation is for the origin to sit at the center of the total dedicated rectangle with
    # angleChange is a bool used to decide whether to reevaluate calculations after a change in rotation,
    # corners is a list containing the position of corners relative to the origin, (updated when orientation is changed)
    def __init__(self, position, coords, rgb, orientation):
        self.position = position
        self.coords = coords
        self.rgb = rgb
        self.getSpace = len(coords) * len(coords[0]) * len(coords[0][0])
        self.rotationMatrix = []
        self.set_orientation(orientation[0], orientation[1], orientation[2], orientation[3])
        self.angleChange = True
        l = len(coords)/2
        self.cornersBase = [[-l, -l, -l],[-l, -l, l],[-l, l, -l],[-l, l, l],[l,-l,-l],[l, -l, l],[l, l, -l],[l, l, l]]

    def get_volume(self):
        v = 0
        for x in range(len(self.coords)):
            for y in range(len(self.coords[0])):
                for z in range(len(self.coords[0][0])):
                    if self.coords[x][y][z]:
                        v += 1
        return v

    # returns the absolute coordinates of corners
    def get_corners(self):
        if self.angleChange:
            newCorners = []
            r = self.rotationMatrix
            for x in range(8):
                newCorners.append(matrix_add(self.position,matrix_mult(r, self.cornersBase[x])))
            return newCorners
        return [self.corners[0] + self.position[0]]

    def set_orientation(self, x, y, z, v):
        self.angleChange = True
        if x ** 2 + y ** 2 + z ** 2 != 1:
            x = x / math.sqrt(x ** 2 + y ** 2 + z ** 2)
            y = y / math.sqrt(x ** 2 + y ** 2 + z ** 2)
            z = z / math.sqrt(x ** 2 + y ** 2 + z ** 2)
            sinv = math.sin(v)
            cosv = math.cos(v)
        self.rotationMatrix = [[cosv + x * x* (1 - cosv), y * x * (1 - cosv) + z * sinv, z * x * (1 - cosv) - z * sinv],
                               [x * y * (1 - cosv) - z * sinv, cosv + y * y * (1 - cosv), z*y* (1 - cosv) + x * sinv],
                               [x * z * (1 - cosv) + y * sinv, y * z * (1 - cosv) - x* sinv, cosv + z * z * (1 - sinv)]]


# creating a globe


def globe(radius):
    cubeCoords = []
    for x in range(radius * 2):
        cubeCoords.append([])
        for y in range(radius * 2):
            cubeCoords[x].append([])
            for z in range(radius * 2):
                if math.sqrt((x - radius) ** 2 + (y - radius) ** 2 + (z - radius) ** 2) < radius:
                    cubeCoords[x][y].append(True)
                else:
                    cubeCoords[x][y].append(False)
    return cubeCoords


def get_shell(coords):
    shellCoords = []
    for x in range(len(coords)):
        shellCoords.append([])
        for y in range(len(coords[x])):
            shellCoords[x].append([])
            for z in range(len(coords)[x][y]):
                if (x or y or z) != (len(coords-1) or 0):
                    if coords[x-1] and coords[x+1] and coords[y-1] and coords[y+1] and coords[z-1] and coords[z+1]:
                        shellCoords[x][y].append(False)
                    else:
                        shellCoords.append(coords[x][y][z])
    return shellCoords


def matrix_mult(A, B):
    if len(A) == len(B[0]):
        m = []
        for x in range(len(B)):
            m.append([])
            for y in range(len(A)):
                sum = 0
                for i in range(len(B[0])):
                    sum += A[i][y]*B[x][i]
                m[x].append(sum)
        return m
    else:
        print("Matrices not matching")


def matrix_add(A,B,scaleA,scaleB):
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        C=[]
        for x in range(len(A)):
            C.append([])
            for y in range(len(A[0])):
                C[x].append(scaleA*A[x][y]+scaleB*B[x][y])
        return C
    else:
        print("matrices not matching")


a = [[1, 0], [1, 2]]
b = [[1,2], [1]]

print(matrix_mult(a,b))
