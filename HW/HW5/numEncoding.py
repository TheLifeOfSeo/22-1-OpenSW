

def ob(num) :
    if num > 1 :
        print(num % 2, end=' ')
        ob(num // 2)
    else :
        print(num % 2)

def oc(num) :
    if num > 1 :
        print(num % 8, end=' ')
        oc(num // 8)
    else :
        print(num % 8)

#2019038094 서도원입니다!

def ox(num) :
    if num > 1 :
        print(printox(num % 16), end=' ')
        ox(num // 16)
    else :
        print(printox(num % 16))

def printox(num) :
    if num < 10 :
        return num
    elif num == 10 :
        return 'A'
    elif num == 11 :
        return 'B'
    elif num == 12 :
        return 'C'
    elif num == 13 :
        return 'D'
    elif num == 14 :
        return 'E'
    elif num == 15 :
        return 'F'


n = input("숫자를 입력하세요 : ")

print(' 2진수 : ', end='')
ob(int(n))
print(' 8진수 : ', end='')
oc(int(n))
print('16진수 : ', end='')
ox(int(n))
