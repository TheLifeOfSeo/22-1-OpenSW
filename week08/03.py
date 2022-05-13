t = 2
outStr = ["",""]
a = ['Open source is source code that is made freely available for possible modification and redistribution.', 'Code is released under the terms of a software license.']



for i in range(0, int(t)) :
    for j in range(0, len(a[i])) :
        x = a[i][j].upper()
        outStr[i] += x
    print("%d] %s" % (i+1, outStr[i]))

#정답