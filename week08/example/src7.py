t = 2
a = ['Open source is source code that is made freely available for possible modification and redistribution.',
     'Code is released under the terms of a software license.']

reverse = ''
for i in range(0,2):
    for c in a[i]:
        reverse = c + reverse
    print("%d] %s" %(i+1,reverse))
    reverse = ''
