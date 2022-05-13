t = 5
a = ['22220228', '20150002', '01010101', '20140230', '11111111']

for i in range(0,t,1):
    year = int(a[i][0] + a[i][1] + a[i][2] + a[i][3])
    month = int(a[i][4] + a[i][5])
    day = int(a[i][6] + a[i][7])
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if day < 1 or day > 31:
            print("%d] %d" % (i + 1,-1))
        else:
            print("%d] %04d/%02d/%02d" % (i + 1,year,month,day))
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day < 1 or day > 30:
            print("%d] %d" % (i + 1,-1))
        else:
            print("%d] %04d/%02d/%02d" % (i + 1,year,month,day))
    elif month == 2:
        if day < 1 or day > 28:
            print("%d] %d" % (i + 1,-1))
        else:
            print("%d] %04d/%02d/%02d" % (i + 1,year,month,day))
    else:
        print("%d] %d" % (i + 1,-1))
