# 딕셔너리 - 관련된 정보를 짝지어 놓은 것

dict_1 = {1:'a', 2:'b'}
dict_2 = {'a':1, 'b':2}
print(dict_1, type(dict_1))
print()
dict_ex = dict(a = 10, b = 20)
print(dict_ex)

# '키'를 통해서 매칭되는 '값'을 인덱싱 가능
my_dict = {}
my_dict[1] = 'a'
my_dict['b'] = 2
my_dict['c'] = 'd'

print(my_dict)

print(my_dict[1])
print(my_dict['b'])
print(my_dict['c'])

# 키워드 del, 키로 참조되는 값을 한 쌍으로 지움.
del my_dict[1]
print(my_dict)
del my_dict['b']
print(my_dict)
del my_dict['c']
print(my_dict)

# .values() 메소드 - 값만 뽑아옴
my_dict = {'k1': 'v1', 'k2': 'v2'}
for val in my_dict.values():
    print(val)

# .keys() 메소드 - 키만 뽑아옴
for key in my_dict.keys():
    print(key)

# .items() 메소드 - 둘 다 뽑아옴
for key, val in my_dict.items():
    print(key, val)
    
scores = {'Sally': 100, 'Kelly': 80}
for key, val in scores.items():
    print(f'{key}: {val}')  
    
# .update() 일치하는 키가 있으면 값 업데이트
# 새로운 키,값 페어는 추가
my_dict = {'a': 10, 'b': 20, 'd': 80}
my_dict2 = {'a': 110, 'b': 40, 'c': 50}
my_dict.update(my_dict2)
print(my_dict) 

# .get() - 키에 매칭되는 값 가져옴
print(my_dict.get('a'))
print(my_dict.get('z'))    # return nothing, so nonetype
print(my_dict)

# 기타
res = my_dict.pop('a')
print(res)
print(my_dict)

del my_dict['b']
print(my_dict)

my_dict = {'a': 110, 'b': 40, 'c': 50}
print(my_dict)
my_dict.clear()
print(my_dict)

my_dict = {'a': 10, 'b': 20, 'c': 30}
print('a' in my_dict)
print('j' in my_dict)
print(10 in my_dict)

# copy
x = {'a': 1}
y = x
y['a'] = 100
print(x)
print(y)

x = {'a': 10, 'b': 20}
y = x.copy()
y['a'] = 100
print(x)
print(y)

# 사용예
fruits_list = [['apple', 1000], ['banana', 2000], ['mango', 8000]]
print(fruits_list[0][0])
print(fruits_list[0][1])

fruits_dict = {'apple': 1000, 'banana': 2000, 'mango': 8000}

what_f = input('What do you want: ')
count = int(input('How many: '))

if what_f in fruits_dict:
    pay = fruits_dict[what_f] * count
    print(f'{count} {what_f}s, Total {pay}')    
else:
    print('We don\'t have that fruit')