# 문자열 변수의 연산
# 문자열로 +, * 연산이 가능하다   

var_str1 = '내 이니셜은'
var_str2 = 'YES입니다!'
var_str3 = 'Na'

print(var_str1, var_str2)
print(var_str1 + var_str2)
print(var_str3 * 5)

# 문자열 특정 위치의 문자를 읽어올 수 있다
# 이를 문자열 인덱싱(indexing)이라고 하며 [인덱스](대괄호)사용한다.
# 인덱스는 0부터 시작하며, 끝부터 인덱싱 하려면 -1에서 한 칸씩 -1함

str_python = 'python'
print(len(str_python))

print(str_python[0])
print(str_python[5])
print(str_python[-1])
print(str_python[-6])

# 문자 하나가 아닌 부분을 잘라내어 읽어올 수 있다
# 이를 문자열 슬라이싱(slicing)이라고 하며 [시작:끝+1] 사용 
# 시작 숫자 생략 - 처음부터, 끝 숫자 생략 - 끝까지

str_python = 'Hello, python!'
print(len(str_python))

print(str_python[0:1])
print(str_python[:5])
print(str_python[7:])

# .split() 문자열을 분리한다
# split 메소드에 인자가 없으면 디폴드값 공백을 기준으로 분리
# 인자가 주어지면 그 인자를 기준으로 분리 

fruit_str = 'apple banana mango lemon grapefruit'
fruits = fruit_str.split()

print(fruits[0])
print(fruits[2])
print(fruits[4])

fruits = fruit_str.split('a')

print(fruits)

# .format() 메소드 사용
# 값을 할당할 위치를 {}(중괄호)로 남겨두고
# format 메소드의 인자로 값을 할당한다

print('What a {} World!'.format('wonderful'))
print('{} X {} = {}'.format(3, 4, 3*4))
print('a is {0} {1} {2}'.format(1, 2, 3))
print('a is {2} {1} {0}'.format(1, 2, 3))
print('My name is {name} {fname}, 나는 {fname} {name}입니다'\
    .format(name = 'Eunsun', fname = 'Yea'))

# 3.6 version 이후부터, format 메소드 대신 f-string을 쓸 수 있다
b = 'b'
print(f'a is {b}')

x, y, z = 1, 2, 3
print(f'a is {x} {y} {z}')
print(f'a is {z} {y} {x}')

name = 'Eunsun'
fname = 'Yea'
print(f'My name is {name} {fname}, 나는 {fname} {name}입니다')

# 기타 메소드
s = 'His name is Mike. Hey, Mike! You look nice, Mike!'
is_start = s.startswith('His')
print(is_start)

is_start = s.startswith('x')
print(is_start)

print(s.find('Mike'))
print(s.rfind('Mike')) # 문장 뒤부터 찾음
print(s.count('Mike'))
print(s.capitalize())  # 첫 글자를 대문자로, 나머지는 소문자로
print(s.title())       # 단어의 첫 글자 대문자
print(s.upper())       # 전체 대문자
print(s.lower())       # 전체 소문자
print(s.replace('Mike', 'Tom'))