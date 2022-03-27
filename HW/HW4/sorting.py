list = [0xa37b, 0x23cc, 0x88d9, 0xbb8f, 0x3a9a]
print(list[-1])

print('정렬 전 데이터 : ', end ='')
[print(hex(i), end = ' ') for i in list]

#2019038094 서도원입니다!

for i in range(0, len(list)) :
    for j in range (i+1, 5) :
        if list[i] > list[j] :
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
    

print('\n정렬 후 데이터 : ', end ='')
[print(hex(i), end = ' ') for i in list]

