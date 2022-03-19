while (True) :
    print("=========================")
    print("1. 입력한 수식 계산")
    print("2. 두 수 사이의 합계")
    mn = int(input())
    num = 0

    if mn == 1 :
        cal = eval(input())
        print("정답 : %d" % (cal))
    elif mn == 2 :
        start = int(input("1번째 숫자를 입력하세요 : "))
        end = int(input("2번째 숫자를 입력하세요 : "))
        for i in range(start, end + 1) :
            num += i
        print(num)