import math
import tkinter
from tkinter import *
from math import *
from random import *
import time

import Shape
from Shape import *
from Observer import *

root = Tk()
root.title("3d")
root.geometry("1000x1000")


my_canvas = Canvas(root, width=1000, height=1000, bg="white")
my_canvas.pack(pady=20)

centerX = 500
centerY = 500

#size of window
xRange = 1000
yRange = 1000

standardRGB = [255,255,255]

space1 = [1000, 1000, 1000]

observer1 = Observer([0, 0, -1000], [0, 0, 1], 0, 45, 45)


def rgbtohex(r,g,b):
    return f'#{r:02x}{g:02x}{b:02x}'


#function rendering 3d objects on a 2d screen where objects consist
#shapes are the objects to be rendered, using the Shape class
def renderFrame(shapes, observer):
    origin = [0, 0, 0]
    space = []
    distance = 0
    for s in shapes:
        corners = dedicate_space(s,observer)
        for x in range(int(corners[0]),int(corners[1])):
            for y in range(int(corners[2]),int(corners[3])):
                my_canvas.create_line(x,y,x+1,y,fill=project_pixel(space,observer,x,y,distance))

def project_pixel(space,observer,x,y,distance):
    xVTot = observer.xFoV
    yVTot = observer.yFoV

    #min and max ratio x/z and y/z
    xRatio = asin((x-xRange/2)/xRange*xVTot)
    x2 = asin((x+1-xRange/2)/xRange*xVTot)
    yRatio = asin((y-yRange/2)/yRange*yVTot)
    y2 = asin((y+1-yRange/2)/yRange*yVTot)

    xStart = int(observer.position[0])
    yStart = int(observer.position[1])
    zStart = int(observer.position[2])
    x = xStart
    y = yStart
    z = zStart
    while sqrt((x-xStart)**2+(y-yStart)**2+(z-zStart)**2) < distance:
        if space[x][y][z][0]:
            return rgbtohex(space[x][y][z][1], space[x][y][z][2], space[x][y][z][3])

    return standardRGB


def dedicate_space(shape,observer):
    corners = shape.get_corners()
    xFoV = observer.xFoV
    yFoV = observer.yFoV
    xMin = xFoV
    xMax = -xFoV
    yMin = yFoV
    yMax = -yFoV
    for x in range(8):
        vector = Shape.matrix_mult(shape.rotationMatrix,Shape.matrix_add(corners[x],shape.position,1,-1))
        angleX = sin(vector[0]/vector[2])
        angleY = sin(vector[1]/vector[2])
        if -xFoV < angleX <xFoV and yFoV < angleY < yFoV:
            if angleX < xMin:
                xMin = angleX
            if angleX > xMax:
                xMax = angleX
            if angleY < yMin:
                yMin = angleY
            if angleY > yMax:
                yMax = angleX
    xMin = centerX+asin(xMin)*centerX
    xMax = centerX+asin(xMax)*centerX
    yMin = centerY+asin(yMin)*centerY
    yMax = centerY+asin(yMin)*centerY

    return [xMin, xMax, yMin, yMax]



