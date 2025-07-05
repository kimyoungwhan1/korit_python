#산술 연산자
num1 = 30
num2 = 12
print(f"num1 + num2 = {num1 + num2}") #덧셈
print(f"num1 - num2 = {num1 - num2}")
print(f"num1 * num2 = {num1 * num2}")
print(f"num1 / num2 = {num1 / num2}") #실수 몫을 반환을 해준다.
print(f"num1 // num2 = {num1 // num2}") #정수 몫을 반환해 준다.
print(f"num1 % num2 = {num1 % num2}") #나머지를 반환해 준다.

#대입 연산자
x = 10
x += 5
x *= 2
x /= 5
x //= 5

#비교 연산자
x = 10
y = 20
z = 10
print(x == z) #True
print(x > y) #False
print(x == y) #Fasle
print(x != z)
print(x <= y)
print(x >= z)

#논리 연산자
a = True
b = False
print(not a and b) #False
print(a or b) #True
print(not b) #True

#조건 연산자(삼항연산자)
a = 10
b = 20
max_value = a if a > b else b #조건 (a > b)가 참이면 a 거짓이면 b max_value에 들어간다.
print(max_value)

#홀수 판별하기
num = 7
result = "짝수" if num % 2 == 0 else "홀수"
print(result)
# 참일 때 반환값 if 조건 else 거짓일 때 반환값





