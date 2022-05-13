t = 5
a = ["22220228", "20150002", "01010101", "20140230", "11111111"]
b = []

for i in range(0, int(t)) :
    y = str(a[i])[0] + str(a[i])[1] + str(a[i])[2] + str(a[i])[3]
    m = str(a[i])[4] + str(a[i])[5]
    d = str(a[i])[6] + str(a[i])[7]
    if int(m) > 12 or int(m) < 1 :
        b.append("-1")
        continue
    if int(m) == 1 or int(m) == 3 or int(m) == 5 or int(m) == 7 or int(m) == 8 or int(m) == 10 or int(m) == 12 :
        if int(d) > 31 :
            b.append("-1")
            continue
    if int(m) == 4 or int(m) == 6 or int(m) == 9 or int(m) == 11 :
        if int(d) > 30 :
            b.append("-1")
            continue
    if int(m) == 2 :
        if int(d) > 28 :
            b.append("-1")
            continue
    b.append("%s/%s/%s" % (y, m, d))

for i in range(0, int(t)) :
    print("%d] %s" % (i+1, b[i]))

