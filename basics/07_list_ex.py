# list 자료형, 대괄호[] 사용

my_list1 = []
my_list2 = [1, 2, 3]
my_list3 = ['a', 'b']
print(type(my_list1))
print(len(my_list1))

str_lst = list('abcdefghijklmnop')
print(len(str_lst))
print(str_lst[0:5])

# list 마지막에 값 추가하기
# list 메소드 사용 .append()
my_list1.append(123)
my_list1.append('abc')
my_list1.append(True)

# 리스트 인덱싱
print(my_list1[0])
print(my_list1[1])
print(my_list1[2])
print(my_list1[-1])
print(my_list1)

# 지정된 인덱스에 값 추가하기
# list 메소드 사용 .insert
my_list1.insert(1, 100)
print(my_list1)

# 리스트 인덱싱으로 위치 지정해서 값 바꾸기
my_list1[-1] = False
my_list1[0] = 3.14
my_list1[2] = 'ABC'
print(my_list1)

# list 값 삭제하기 .pop() - 디폴트, 마지막 인덱스 값
# 삭제한 값을 리턴
# .pop(index) - 지정된 인덱스 값 제거
print(my_list1.pop())
my_list1.pop(1)
print(my_list1)

# 리스트 값 제거
# 키워드 del 사용
my_list1 = [123, 'abc', True]

del my_list1[0]
print(my_list1)

del my_list1[-1]
print(my_list1)

del my_list1

# 해당 값을 찾아 제거 .remove(값)
my_list1 = [1, 2, 2, 3, 4, 2]
my_list1.remove(2)
print(my_list1)
my_list1.remove(2)
print(my_list1)
my_list1.remove(2)
print(my_list1)
# my_list1.remove(2)
# print(my_list1)

# 리스트 덧셈, 확장
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
x = a + b
print(x)
a += b
print(a)
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
x.extend(y)
print(x)
print(x[::2])  # 인덱스 하나씩 뛰어넘어서
print(x[::-1]) # 뒤에서부터

# 리스트 슬라이싱
my_list1 = [123, 'abc', True]
print(my_list1[:1])
print(my_list1[1:3])
print(my_list1[2:])

my_list1[1:3] = ['ABC', False]
print(my_list1)

my_list1[0:1] = []
print(my_list1)

my_list1[:] = []
print(my_list1)

# 중첩된 리스트
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = [a, n]
print(x)
print(x[0])
print(x[1])
print(x[0][1])
print(x[1][3])

# 리스트 정렬
# .sort() 메소드 사용
# 리턴 값 없음. 호출한 리스트 정렬 
my_list = [10, 1, 5, 4, 2]
my_list.sort()
print(my_list)

my_list = ['mango','stawberry', 'elderberry','banana','apple']
my_list.sort()
print(my_list)

my_list.sort(reverse=True)
print(my_list)

my_list.reverse() # 리스트 순서 거꾸로
print(my_list)

# 리스트 요소 개수 새기
# .count() 메소드 사용
my_list = ['a', 'b', 'c', 'a', 'a']
print(my_list.count('a'))

# 키워드 in, not in
my_list = ['a', 'b', 'c', 'd', 'e']
print('a' in my_list)
print('d' not in my_list)
print('f' not in my_list)

# 값을 찾아 인덱스 리턴 .index()
my_list = [1, 2, 3, 4, 5, 1, 2, 3]
print(my_list.index(3)) # 값 3을 찾아 인덱스 리턴
print(my_list.index(3, 4)) # 인덱스 4부터 값 3을 찾아 인덱스 리턴

# split & join
my_str = 'Today is Sunday'
splitted = my_str.split()
print(splitted, type(splitted))

splitted = my_str.split('!!!')
print(splitted)

splitted = my_str.split(' ')
print(splitted)

x = ' '.join(splitted)
print(x)

x = '###'.join(splitted)
print(x)

# 리스트와 참조
a = [1, 2, 3, 4, 5]
b = a
b[0] = 100
print('a = {}'.format(a), 'id of a = {}'.format(id(a)))
print('b = {}'.format(b), 'id of b = {}'.format(id(b)))

# copy 메소드
x = [1, 2, 3, 4, 5]
y = x.copy()
y[0] = 100
print('x = {}'.format(x), 'id of x = {}'.format(id(x)))
print('y = {}'.format(y), 'id of y = {}'.format(id(y)))

# 다른 변수의 경우
c = 20
d = c
print(c)
print(d)
print(id(c))
print(id(d))

d = 10
print(c)
print(d)
print(id(c))
print(id(d))
