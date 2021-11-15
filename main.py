import time
import turtle #Successfully installed PyYAML-6.0 turtle-0.0.1
#import math
import random
wn = turtle.Screen()
wn.bgcolor('black')

class MainVar():#p.a.c.v.
    start_size_num = 10
    size_change = 10
    circles_inside = 7



list16 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
def randColor():
    rand_color_list = ['#']
    for i in range(6):
        rand_color_list.append(random.choice(list16))
    colour = ''.join(rand_color_list)
    return colour


def drawCircle(t, size, circles_inside):
    for i in range(circles_inside):
        t.circle(size)
        size = size - 2# #MainVar.size_differ_num += 1
        print("size ", size)

def drawSpecial(t, size, repeat, circles_inside):
    for i in range(repeat):
        drawCircle(t, size, circles_inside)
        t.right(360/repeat)

while(True):
    Model = turtle.Turtle()
    Model.speed(0)
    Model.color(randColor())
    drawSpecial(Model,MainVar.start_size_num,10, MainVar.circles_inside)
    MainVar.start_size_num += MainVar.size_change





