# 변수를 선언하고 그 값과 자료형을 출력합니다

# 정수형
var_int1 = 34
var_int2 = 0
var_int3 = -34

print(var_int1, type(var_int1))
print(var_int2, type(var_int2))
print(var_int3, type(var_int3))

# 실수형 
var_float1 = 3.14
var_float2 = 0.0
var_float3 = -3.14

print(var_float1, type(var_float1))
print(var_float2, type(var_float2))
print(var_float3, type(var_float3))

# 문자열
var_str1 = 'YES'
var_str2 = "I'm a teacher of Oryu Coding Club"

print(var_str1, type(var_str1))
print(var_str2, type(var_str2))

# 불리언형
var_bool1 = True
var_bool2 = False

print(var_bool1, type(var_bool1))
print(var_bool2, type(var_bool2))

# 변수 타입 바꾸기 1
num = 1
name = "Yea Eunsun"

num = name
print(type(num))

# 변수 타입 바꾸기 2
num2 = 123
num2 = str(num2)
print(num2, type(num2))
num2 = float(num2)
print(num2)