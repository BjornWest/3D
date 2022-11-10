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
        self.corners = []

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
            l = len(self.coords) / 2
            r = self.rotationMatrix
            self.corners = [[-l*r[1][1], -l, -l], [l, -l, -l], [-l, l, -l], [-l, -l, l],[-l, l, l], [l, -l, l],[l, l, -l], [l, l, l]]
            return []
        return [self.corners[0] + self.position[0]]

    def set_orientation(self, x, y, z, v):
        self.angleChange = True
        if x ** 2 + y ** 2 + z ** 2 != 1:
            x = x / math.sqrt(x ** 2 + y ** 2 + z ** 2)
            y = y / math.sqrt(x ** 2 + y ** 2 + z ** 2)
            z = z / math.sqrt(x ** 2 + y ** 2 + z ** 2)
        self.rotationMatrix = [[math.cos(v) + x * x * (1 - math.cos(v)), x * y * (1 - math.cos(v)) - z * math.sin(v),
                                x * z * (1 - math.cos(v)) + y * math.sin(v)],
                               [y * x * (1 - math.cos(v)) + z * math.sin(v), math.cos(v) + y * y * (1 - math.cos(v)),
                                y * z * (1 - math.cos(v)) - x * math.sin(v)],
                               [z * x * (1 - math.cos(v)) - z * math.sin(v),
                                z * y * (1 - math.cos(v)) + x * math.sin(v), math.cos(v) + z * z * (1 - math.cos(v))]]


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
