import turtle as t

swidth, sheight = 1000, 1000

if __name__ == "__main__" :
    t.title('구구단')
    t.shape('turtle')
    t.setup(width = swidth, height = sheight)
    t.screensize(swidth, sheight)
    t.penup()
    tX, tY = -500, 250
    t.goto(tX, tY)

    for i in range (1, 10) :
        for j in range (2, 10) :
            t.goto(tX + 80 * j, tY - 40 * i)
            gugu = str(j) + 'x' + str(i) + '=' + str(j * i)
            t.write(gugu, font = ('Arial', 12, 'bold'))

    t.done()