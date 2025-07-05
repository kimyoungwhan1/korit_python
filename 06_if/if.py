#조건문
"""

if 조건:
    실행할 코드
"""
num = int(input("숫자를 입력하세요 : ")) #input은 문자열이라서 숫자 0보다 큰지 비교가 불가능하다. 그래서 int로 변환하고 비교해야 한다.
if num > 0:
    print("양수 입니다.") #해당 조건이 참 일 때
else: #해당 조건이 거짓 일 때
    print("이 숫자는 0이거나 음수입니다.")

#if - elif - else문
score = int(input("점수를 입력하세요 : "))

if score >= 90:
    print("A 학점입니다.")
elif score >= 80:
    print("B 학점입니다.")
elif score >= 70:
    print("C 학점입니다.")
elif score >= 60:
    print("D 학점입니다.")
else:
    print("F 학점입니다.")

#실습
#숫자를 입력받아서 조건문으로 홀 짝 판별하기
num = int(input("숫자를 입력하세요: "))
if num % 2 == 0:
    print("짝수")
else:
    print("홀수")

#나이를 입력받고 성인여부 입력 받기 (Y/N)
#20세 이상이면서 성인이면 성인학생입니다. 아니면 성인 학생이 아닙니다.
age = int(input("나이를 입력해 주세요 : "))
student = input("학생인가요? - (Y/N) : ")

if age >= 20 and student == "y":
    print("성인학생 입니다.")
else:
    print("성인학생이 아닙니다.")



