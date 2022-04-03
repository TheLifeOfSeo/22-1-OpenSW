data = ['A37B', '23CC', '88D9', 'BB8F', '3A9A']


def getNumber(x) :
    num = ''
    for i in x :
        if i.isdigit() :
            num += i
    return int(num)

#2019038094 서도원입니다!

for i in range(0, len(data)) :
    for j in range (i+1, 5) :
        if getNumber(data[i]) > getNumber(data[j]) :
            temp = data[i]
            data[i] = data[j]
            data[j] = temp


print('\n정렬 후 데이터 : ', end ='')
[print(i, end = ' ') for i in data]
