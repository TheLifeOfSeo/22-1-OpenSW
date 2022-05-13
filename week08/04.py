a = []

for i in range(1,100) :
    k = 0
    for j in range(2, int(i)) :
        if i % j == 0 :
            k = k + 1
    if k == 0 :
        a.append(i)

for i in range(1, len(a)) :
    print(a[i],end = ' ')


#정답