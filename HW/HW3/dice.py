import random
dice = [0,0,0,0,0,0]
count = 0
x = 0
while(x == 0) :
    for i in range (0, 6):
        dice[i] = random.randrange(1, 7)
    count += 1
    #반복문 1,2 2,3 ~~~ 5,6 같은지 비교 후 같으면 stop 
    for i in range (0, 5):
        if dice[i] != dice[i+1] :
            x = 0
            break
        else :
            x = 1
            continue


for i in range (6) :
    print("%d번 주사위 : %d" % (i + 1, dice[i]))
print ("총 비교 횟수 : %d" % (count))