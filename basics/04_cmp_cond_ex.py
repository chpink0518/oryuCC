# 불리언 - 참/거짓
my_bool1 = True
my_bool2 = False
my_bool3 = 1 < 2
my_bool4 = 1 == 2

my_bools = my_bool1, my_bool2, my_bool3, my_bool4
my_blist = []
my_blist = list(my_bools)

print(my_bools)
print(my_blist)

# 비교연산 - 결과는 참 혹은 거짓
my_cmp1 = 1 < 2
my_cmp2 = 1 == 2
my_cmp3 = 2 <= 1
my_cmp4 = 1 <= 2 < 3
my_cmp5 = 5 <= 2 < 3

my_cmps = my_cmp1, my_cmp2, my_cmp3, my_cmp4, my_cmp5

print(my_cmps)

# and, or, not
my_con1 = True and True
my_con2 = True and False
my_con3 = True or False
my_con4 = not True

my_cons = my_con1, my_con2, my_con3, my_con4

print(my_cons)

# 비교연산과 and, or, not의 결합

my_con1 = 1 < 2 and 2 < 3
my_con2 = 1 < 2 and 2 > 1
my_con3 = 1 < 2 or 2 < 1
my_con4 = not 1 == 1

my_cons = my_con1, my_con2, my_con3, my_con4

print(my_cons)

# 이름을 입력받아 코딩 동아리 강사인지 학생인지 판별
coding_club = ['stu1', 'stu2', 'stu3', 'stu4', 'stu5', 'stu6', 'stu7', 'stu8']

name = input('name: ')
if name == 'YES':
    print('당신이 강사 YES군요!')
    print('학생들을 열심히 가르치세요! ^^')
elif name in coding_club:
    print('당신은 코딩 동아리 학생이군요')
    print('열심히 공부해서 멋진 게임을 만들어봐요! >ㅁ<')
else:
    print("누구세요? @ㅁ@")