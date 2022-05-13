word = input('원하는 문장 입력해주세요 : ')
reverse = ''
for i in range (0, len(word)) :
    print(word[(len(word) - 1) - i], end = '')
    reverse += word[len(word) - 1 - i]

print(reverse)