t = 10
a = [9, 15, 54, 369, 634, 1053, 2954, 4234, 5424, 9531]

total = 0
for i in range(0, t):
    for n in range(1,a[i]+1):
        total += n
    print("%d] %d" %(i+1, total))
    total = 0
