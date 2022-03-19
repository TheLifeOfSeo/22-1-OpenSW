import turtle as t

num = int(input("숫자를 입력하세요. : "))
biNum = format(num, 'b')
swidth, sheight = 1000, 300
tx,ty = 0,0 #거북이의 최초 좌표

#2019038094 서도원

t.title('거북이 2진수 표현')
t.shape('turtle')
t.setup(width = swidth + 50, height = sheight + 50) #창 크기
t.screensize(swidth,sheight) #영역 크기 1000,300
t.penup() #이동 궤적 그려지지 않게 설정
t.left(90) #거북이가 위로 향하게 설정
t.stamp() #거북이 도장 찍기



for i in range(len(biNum)) :
    t.goto(tx, ty)
    if num & 1 :
        t.color('red')
        t.turtlesize(2)
    else :
        t.color('blue')
        t.turtlesize(1)
    t.stamp()
    tx -= 50
    num >>= 1

t.done()