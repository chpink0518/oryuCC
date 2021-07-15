# while문의 기본
count = 0

while count < 3:
    print('횟수:', count)
    count = count + 1

# while + continue
# continue: 아래줄로 내려가지 않고 다시 루프의 처음으로 돌아감
count = 0

while count < 5:
    count += 1          # count = count + 1
    if count % 2 == 1:
        continue
    print(count)   

# while + break
# loop를 빠져나감
while True:
    name = input('이름이 뭐예요?: ')
    if name == 'fin':
        print('이제 모두 안녕~!')
        break
    print('{}님, 안녕!'.format(name))

# 숫자 입력 받기
age = int(input('당신의 나이는? :'))
print('{}살 이시군요!'.format(age))