import turtle as t
import random
import math

from tkinter.simpledialog import *

inStr = ''
swidth, sheight = 1000, 1000
tX, tY, txtSize = [0] * 3
range = 0

t.title('거북이놀이')
t.shape('turtle')
t.setup(width = swidth + 50, height = sheight + 50)
t.screensize(swidth, sheight)
t.penup()

inStr = askstring('문자열 입력', '거북이 쓸 문자열을 입력')

range = len(inStr)

for ch in inStr :
    range -= 1
    tX = 400 * (range / len(inStr)) * math.cos(3.14 / 180 * (720 * range / len(inStr)))
    tY = 400 * (range / len(inStr)) * math.sin(3.14 / 180 * (720 * range / len(inStr)))
    r = random.random();
    g = random.random();
    b = random.random();
    txtSize = random.randrange(10, 50)

    t.goto(tX,tY)

    t.pencolor((r,g,b))
    t.write(ch, font=('맑은 고딕', txtSize, 'bold'))

t.done()