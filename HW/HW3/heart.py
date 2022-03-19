x = []

num = str(input("양의 정수를 입력하세요 : "))

for i in num :
    x.append(int(i))

for i in x :
    heartStr = ""
    for j in range(0, i) :
        heartStr += "🔥"
    print(heartStr)

