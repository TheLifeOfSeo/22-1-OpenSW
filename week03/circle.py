#원그리기

import turtle as t
swidth, sheight = 500, 500

t.title('무지개색 원그리기')
t.shape('turtle')
t.setup(width = swidth + 50, height = sheight + 50)
t.screensize(swidth, sheight)
t.penup()
t.goto(0, -sheight/2)
t.pendown()
t.speed(10)

for radius in range(1,250) :
    if radius % 6 == 0 :
        t.pencolor('red')
    elif radius % 4 == 0 :
        t.pencolor('blue')
    elif radius % 3 == 0 :
        t.pencolor('green')
    elif radius % 2 == 0 :
        t.pencolor('navy')
    elif radius % 1 == 0 :
        t.pencolor('yellow')
    else :
        t.pencolor('purple')
    t.circle(radius)

t.done()
