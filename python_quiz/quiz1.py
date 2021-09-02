import arrow

b_year, b_month, b_day = map(int, input("생년월일을 '년 월 일' 형식으로 입력하세요: ").split())

now = arrow.now()

man_age = now.year - b_year

if now.month < b_month:
    man_age -= 1
elif now.month == b_month and now.day < b_day:
    man_age -= 1
        
print(f'당신의 만 나이는 {man_age}입니다')

