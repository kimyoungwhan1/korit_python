#반복문 (while)
"""
while 조건:
    반복할 코드
    (조건을 변경하는 코드)
"""
num = 1
while num <= 5: #참일 경우 무한 반복
    print("숫자:", num)
    num += 1 #이걸 넣어줌으로 써 무한 반복은 안되고 5까지만 출력된다.

num = 1
while num <= 10:
    print(num)

    if num == 5:
        break #반복중 특정 조건에서 멈추고 싶을 경우

    num += 1

num = 0
while num < 10:
    num += 1
    #3의 배수는 출력하지 않겠다. 3의 배수를 알 수있는 조건은 나눠서 나머지가 3의 배수인것들이니까
    if num % 3 == 0:
        continue #3일 때 continue 만나서 다시 올라간다. 4, 7 10부터 다시 출력됨

    print(num) #더하기를 먼저하고 출력해서 2부터 나온다. num이 10미만 이라 출력되면 안되는데 9였을 때 출력된거다.

dan = 1
while dan <= 9:
    n = 1
    while n <= 9:
        print(f"{dan} X {n} = {dan * n}")
        n += 1
    dan += 1

#실습
#1부터 100까지 짝수만 출력하기
num = 1
while num <= 100:
    if num % 2 == 0:
        print(num)
    num += 1
#5의 배수 50까지 출력하기 (30에서 멈추기)









