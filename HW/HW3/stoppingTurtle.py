import turtle as t
import math
import random


swidth, sheight = 1000, 1000

T = [None, None, None] #거북이 3마리
distance = [0,0,0] #거북이간 거리
tX, tY = [0,0,0], [0,0,0] #각 거북이 좌표


if __name__ == "__main__" :
    t.title('거북이 충돌')
    t.setup(width = swidth + 50, height = sheight + 50)
    t.screensize(swidth, sheight)
    t.penup
    
    T[0] = t.Turtle('turtle'); T[0].color('red'); T[0].penup;
    T[1] = t.Turtle('turtle'); T[1].color('green'); T[1].penup;
    T[2] = t.Turtle('turtle'); T[2].color('blue'); T[2].penup;

    T[0].goto(-200, -200)
    T[1].goto(0,0)
    T[2].goto(200,200)

    while True :
        angle = random.randrange(0, 360)
        dist = random.randrange(1,50)
        T[0].left(angle)
        T[0].forward(dist)
        angle = random.randrange(0, 360)
        dist = random.randrange(1,50)
        T[1].left(angle)
        T[1].forward(dist)
        angle = random.randrange(0, 360)
        dist = random.randrange(1,50)
        T[2].left(angle)
        T[2].forward(dist)

        for i in range(0,3) :
            tX[i] = T[i].xcor(); tY[i] = T[i].ycor()
        
        distance[0] = ((tX[0] - tX[1]) * (tX[0] - tX[1])) + ((tY[0] - tY[1]) * (tY[0] - tY[1]))
        distance[1] = ((tX[1] - tX[2]) * (tX[1] - tX[2])) + ((tY[1] - tY[2]) * (tY[1] - tY[2]))
        distance[2] = ((tX[2] - tX[0]) * (tX[2] - tX[0])) + ((tY[2] - tY[0]) * (tY[2] - tY[0]))

        for i in range (0,3) :
            if distance[i] < 20 :
                T[0].turtlesize(3)
                T[1].turtlesize(3)
                T[2].turtlesize(3)
                break

t.done