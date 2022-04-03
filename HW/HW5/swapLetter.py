# 대소문자 상호 변환


if __name__ == "__main__" :
    word = input('문자열을 입력하세요 : ')

#2019038094 서도원입니다!

    for i in range(len(word)) :
        if ord(word[i]) >= ord('a') and ord(word[i]) <= ord('z'):
            print(word[i].upper(), end='')
        elif ord(word[i]) >= ord('A') and ord(word[i]) <= ord('Z'):
            print(word[i].lower(), end='')
        else :
            print(word[i], end='')
