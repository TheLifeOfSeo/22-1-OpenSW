import random
import turtle


def leftClick(x,y) :
    global r, g, b
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.color((r,g,b))
    size = random.randrange(1, 10)
    turtle.right(random.randrange(1,90))
    turtle.shapesize(size)
    turtle.goto(x,y)
    turtle.stamp()


#2019038094 서도원


thickness, size = 1, 0
r, g, b = 0.0, 0.0, 0.0

# turtle.title('거북이 흔적 남기기')
turtle.shape('turtle')
turtle.pensize(thickness)

turtle.onscreenclick(leftClick, 1) #우클릭 대신 좌클릭으로 설정했습니다.

turtle.done()