from re import A


print('세 정수의 값을 입력해주시면 최대값을 출력합니다.')

a = input('첫 번째 정수 : ')
b = input('두 번째 정수 : ')
c = input('세 번째 정수 : ')

maximum = a

if maximum < b : maximum = b
if maximum < c : maximum = c

print('최대값은 ' + maximum + '입니다')