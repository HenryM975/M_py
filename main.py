import turtle #Successfully installed PyYAML-6.0 turtle-0.0.1
import math
import random
wn = turtle.Screen()
wn.bgcolor('black')

size_differ_num = 1
color_list = ['white', 'yellow', 'blue', 'orange', 'pink', 'green', 'red', 'purple', 'black', '#6DF405', '#5CCEC8', '#BBF876', '#ADE7E5', '#F20765', '#9B012C', '#EB08EF', '#D8B206', '#9D87B5']
color_list_num = 0
size_num = 10

while(True):
    Model = turtle.Turtle()
    Model.speed(0)
    Model.color(random.choice(color_list))#?
    rotate = int(360)
    def drawCircle(t, size):
        for i in range(10):
            t.circle(size)
            size = size - size_differ_num
            print("size ", size)
    def drawSpecial(t, size, repeat):
        for i in range(repeat):
            drawCircle(t, size)
            t.right(360/repeat)
    drawSpecial(Model,size_num,10)
    size_differ_num+=1
    color_list_num+=1
    print(size_num)
    size_num += 10



