import operator

word = '내가 그의 이름을 불러주기 전에는 그는 다만 하나의 몸짓에 지나지 않았다. 내가 그의 이름을 불러주었을 때, 그는 나에게로 와서 꽃이 되었다. 내가 그의 이름을 불러준 것처럼 나의 이 빛깔과 향기에 알맞은 누가 나의 이름을 불러다오. 그에게로 가서 나도  그의 꽃이 되고 싶다. 우리들은 모두 무엇이 되고 싶다. 너는 나에게 나는 너에게 잊혀지지 않는 하나의 눈짓이 되고 싶다.'
dict = {}
list = []

# print('원문 : ' + word)

# 한 글자씩 입력받아서
# 없는 글자 = 딕셔너리 새로 만들기
# 있는 글자 = 딕셔너리 1 증가
# 전체 순서대로 정렬 후 출력


#2019038094 서도원입니다!


for i in range(len(word)) :
    if 'ㄱ' <= word[i] and word[i] <= '힣' :
        if word[i] in dict :
            dict[word[i]] += 1
        else :
            dict[word[i]] = 1


list = sorted(dict.items(), key = operator.itemgetter(1), reverse = True)

print('문자\t빈도수')
print('----------------')
for i in range(0, len(list)) :
    print(list[i][0], '\t', list[i][1])