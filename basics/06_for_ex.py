# for with list
my_list = [1, 2, 3]
for count in my_list:
    print('횟수:', count)

# for with string
my_str = 'coding'
for letter in my_str:
    print('문자:', letter)

# for with range
print(range(3))
print(list(range(3)))

print('------------------')
for test in range(3):
    print('횟수:', test)
print('------------------')
for st_test in range(0, 3):
    print('횟수:', st_test)
print('------------------')
for st_test in range(5, 10):
    print('횟수:', st_test) 
print('------------------')
for i in range(2, 10, 3):
    print(i)
print('------------------')
for i in range(10, 1, -3):
    print(i)
print('------------------')

# 중복된 for loop
for j in range(2):
    for i in range(2):
        print(f'i: {i}, j: {j}')

# 인덱스를 변수로 사용하지 않는 경우, _로 표시    
for _ in range(3):
    print('hello')
     
# enumerate, zip 함수   
days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'orange', 'banana']
foods = ['egg', 'chicken', 'salad']

for i, fruit in enumerate(fruits):
    print(i, fruit)
    
print()

for day, fruit, food in zip(days, fruits, foods):
    print(day, fruit, food)