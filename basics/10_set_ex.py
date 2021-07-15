# 중복되는 내용 자동 제거
my_set1 = {1, 2, 2, 3, 4, 5, 3, 1, 6, 7, 8, 6}
print(my_set1)
print(type(my_set1))

my_set2 = {1, 2, 3, 3, 4, 5, 5, 9, 10, 11}
print(type(my_set2))

# 차집합
res = my_set1 - my_set2 
print(res)

res = my_set2 - my_set1
print(res)

# 교집합
res = my_set1 & my_set2 
print(res)

# 합집합
res = my_set1 | my_set2 
print(res)

# 집합의 대칭 차이: 합집합 - 교집합
res = my_set1 ^ my_set2 
print(res)

# add, remove, clear
s = {1, 2, 3, 4, 5}
s.add(6)
print(s)
s.add(6)
print(s)
s.remove(6)
print(s)
s.clear()
print(s, type(s))

# + 연산은 불가, - 연산만 가능
k = {'a', 'b'}
j = {'a', 1, True}
print(k - j)
print(j - k)

# 사용예 1: 공통 친구 찾기
friends_of_a = {'Mike', 'James', 'Lucy'}
friends_of_b = {'James', 'Harry', 'Anna'}

both = friends_of_a & friends_of_b
print(both)

# 사용예 2: 전체 과일 구매 리스트로부터 종류만 얻기
fr_buy_list = ['apple', 'banana', 'banana', 'orange', 'mango', 'apple']
fr_kind = set(fr_buy_list)
print(fr_kind)
