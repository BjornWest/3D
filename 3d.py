import math
import tkinter
from tkinter import *
from math import *
from random import *
import time
from Shape import *
from Observer import *

root = Tk()
root.title("Cosmopol")
root.geometry("1000x1000")


my_canvas = Canvas(root, width=1000, height=1000, bg="white")
my_canvas.pack(pady=20)

centerX = 500
centerY = 500

#size of window
xRange = 1000
yRange = 1000

space1 = [1000, 1000, 1000]

observer1 = Observer([0, 0, -1000], [0, 0, 1], 0, 45, 45)

#function rendering 3d objects on a 2d screen where objects consist
#shapes are the objects to be rendered, using the Shape class
def renderFrame(space,shapes, observer):
    origin = [0, 0, 0]
    xRange = 1000
    yRange = 1000
    fullSpace = []
    for x in range(space[0]):
        for y in range(space[1]):
            for z in range(space[2]):

    for y in range(yRange):
        for x in range(xRange):



    root.update()

