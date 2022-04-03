word = '파이썬은완전재미있어요'
print(word)

for i in range (len(word)) :
    if i % 2 == 0 :
        print(word[i], end='')
    elif i % 2 == 1 :
        print('#', end='')