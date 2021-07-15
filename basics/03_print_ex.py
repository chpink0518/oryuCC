# print 함수 좀 더 알아 보기

# 출력의 끝 지정하기 - 줄바꿈이 기본
print('coding', end = '')
print('coding', end = '-')
print('coding', end = '\n')
print('coding', end = '\t')
print('coding')

# 여러줄에 걸친 문자열 출력
print('''이 문장은 두 줄로 이어지지만
하나의 print함수로 출력됩니다.''')
print("""BlackPink
in your area!""")

# 문자열에 '', "" 둘 다 사용하는 이유
print("I'm a teacher")
print('"안녕하세요?"라며 밝은 얼굴로 인사하는 학생들')

# 다른 방법도 있다
print('I\'m a student')
print("say \"Hello, peter\"")

# 파일 경로를 이스케이프 코드 상관없이 raw type으로 표시할 때
print(r'C:\name\name\test')

# C언어 스타일 포매팅
# %d - 정수, %f - 실수, %s - 문자열
print('What a %s World!' % 'wonderful')
print('%d X %d = %d' % (2, 3, 2*3))
