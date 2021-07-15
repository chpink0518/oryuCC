# 튜플 - 소괄호 사용, 값을 바꿀 수 없다
# 소괄호 생략 가능
# 튜플 요소의 개수가 하나라면 끝에 콤마를 붙여줘야 튜플로 인식
# 아니면 그냥 요소의 자료형으로 인식하기 때문에 꼭 필요함
my_tuple1 = ()
my_tuple2 = (1,)
print(type(my_tuple2))
my_tuple2 = (1)
print(type(my_tuple2))
# error! tuple does not support item assignment
# my_tuple2[0] = 100  

# 튜플 인덱싱, 슬라이싱, 메소드
my_tuple = (1, 2, 3, 4, 1, 2)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[2:])
print(my_tuple.index(1))
print(my_tuple.index(1, 2))
print(my_tuple.count(1))

# 튜플 내의 리스트 값은 수정 가능
my_tuple = (['a', 'b', 'c'], 3, [1, 2, 3])
print(my_tuple[0][0])
my_tuple[0][0] = 'k'
print(my_tuple[0][0])
print(my_tuple[2][0])
my_tuple[2][0] = 100
print(my_tuple[2][0])

# 튜플 패킹, 언패킹
my_tuple4 = 3.14, 'python', True    # packing
a, b, c = my_tuple4                 # unpacking

print(my_tuple4)
print(f'a = {a}, b = {b}, c = {c}')

# 일반적인 변수 값 바꾸기
i = 10
j = 20
tmp = i
i = j
j = tmp
print(i, j)

# 언패킹을 이용한 값 바꾸기
a = 100
b = 500
a, b = b, a
print(a, b)

# 온라인 시험, 정답은 변경 안 되는 튜플에!
answer = ('a', 'c')
answered = []

print('Choose 2 of 3 : a, b, c')

for i in range(2):    
    res = input('Your choice {}: '.format(i+1))
    answered.append(res)

print('Your answer is', answered)

if answered[0] in answer:
    if answered[1] in answer:
        print('Your answer is correct!')
    else:
        print('You choosed the wrong answer')        
else:
    print('You choosed the wrong answer')