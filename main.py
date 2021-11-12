import turtle #Successfully installed PyYAML-6.0 turtle-0.0.1
#import math
import random
wn = turtle.Screen()
wn.bgcolor('black')



list16 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
def randColor():
    rand_color_list = ['#']
    for i in range(6):
        rand_color_list.append(random.choice(list16))
    colour = ''.join(rand_color_list)
    return colour


def drawCircle(t, size):
    for i in range(10):
        t.circle(size)
        size = size - size_differ_num
        print("size ", size)

def drawSpecial(t, size, repeat):
    for i in range(repeat):
        drawCircle(t, size)
        t.right(360/repeat)


size_differ_num = 1
size_num = 10

while(True):
    Model = turtle.Turtle()
    Model.speed(0)
    Model.color(randColor())
    rotate = int(360)
    drawSpecial(Model,size_num,10)
    size_differ_num += 1
    size_num += 10




