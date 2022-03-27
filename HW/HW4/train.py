import operator


train = [('토마스', 5),
        ('헨리', 8),
        ('에드워드', 9),
        ('에밀리', 5),
        ('토마스', 4),
        ('헨리', 7),
        ('토마스', 3),
        ('에밀리', 8),
        ('퍼시', 5),
        ('고든', 13)]

currentRank, totalRank = 1,0
dictTrain = {}

for i in train :
    tKey = i[0]
    tValue = i[1]
    if tKey in dictTrain :
        dictTrain[tKey] += tValue
    else :
        dictTrain[tKey] = tValue

trainList = sorted(dictTrain.items(), key = operator.itemgetter(1), reverse = True)

print('-------------------------------')
print("기차 수송량 목록")
print(train)
print('-------------------------------')
print('기차\t총수송량\t순위')
print('-------------------------------')

for i in range(0, len(trainList)) :
    totalRank += 1
    if trainList[i][1] == trainList[i-1][1] :
        pass
    else :
        currentRank = totalRank
    print(trainList[i][0], '\t', trainList[i][1], '\t', currentRank)




#튜플을 딕셔너리로 바꾼 후 정렬 후 정렬된 딕셔너리를 튜플로 변환




