
t = 2
a = ['Open source is source code that is made freely available for possible modification and redistribution.', 'Code is released under the terms of a software license.']
b = ['','']
k = 0
for i in range(0, int(t)) :
    for j in range(len(a[i]) - 1, -1, -1) :
        b[i] += a[i][j]


for i in range(0, int(t)) :
    print("%d] %s" % (i+1, b[i]))
