import sys

int1, float1, bool1, str1, list1, tuple1, dict1, set1 = [None] * 8


#2019038094 서도원

int1 = 0
float1 = 0.0
bool1 = True
str1 = ''
list1 = []
tuple1 = ()
dict1 = {}
set1 = set()

print("int형의 기본 크기 -> ", sys.getsizeof(int1))
print("float형의 기본 크기 -> ", sys.getsizeof(float1))
print("bool형의 기본 크기 -> ", sys.getsizeof(bool1))
print("string형의 기본 크기 -> ", sys.getsizeof(str1))
print("list형의 기본 크기 -> ", sys.getsizeof(list1))
print("tuple형의 기본 크기 -> ", sys.getsizeof(tuple1))
print("dictionary형의 기본 크기 -> ", sys.getsizeof(dict1))
print("set형의 기본 크기 -> ", sys.getsizeof(set1))