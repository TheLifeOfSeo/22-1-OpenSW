t = 10
a = [9, 15, 54, 369, 634, 1053, 2954, 4234, 5424, 9531]
b = [2, 6, 6, 15, 20, 34, 50, 89, 123, 9999]
num = [0,0,0,0,0,0,0,0,0,0]

for i in range(0,int(t)) :
    if a[i] > b[i] :
        c = a[i]
    else :
        c = b[i]
    for j in range(1, int(c)) :
        if (a[i] % j == 0 and b[i] % j == 0 and j > num[i]) :
            num[i] = j
    print("%d] %d" % (i+1, num[i]))


#정답