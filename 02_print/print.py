#사용자에게 입력 받기 위한 함수
#input()
from streamlit.runtime.metrics_util import gather_metrics

a = input()
print("내가 입력한 것 : " + a)

username = input("이름을 입력하세요 : ")
print("사용자 이름 : " + username)

age = input("나이를 입력하세요 : ")
print(type(age))
print("사용자 나이 : " + age)
#이렇게 하면 잘 나오지만 input으로 입력받은 모든 값은 다 문자열로 된다. 그러니 age가 정수인데 정수로 넣어도 문자열 형태로 된다.

#출력하기 다양한 방식
last_name = "김" #문자열
first_name = "영환" #문자열
name = last_name + first_name
age = 27 #int(정수형)
phone_number = "01012345678" #숫자는 맨 앞에 0이 나올 수 없다.

print("hi" + "hello" + "world") #이렇게 출력하면 다 붙어 있을 것이다. 띄우기 위해서는 ,를 써줘도 가능하다
print("hi", "hello", "world")
print("내 전화번호는 " + phone_number + " 입니다.")
print("제 나이는 " + age + "입니다.") #age밑에 밑줄은 경고를 주는 표시이다. str이 나올 줄 알았는데 int가 들어가 있기 때문
print("제 나이는 {} 입니다.".format(age)) #이렇게 하면 age사용 가능해진다.
print("제 이름은 {}, 나이는 {} 입니다.". format(name, age)) #여러개를 쓰는 방법, 순서만 맞춰주면 된다.
print("제 이름은 {nm}, 나이는 {age} 입니다.".format(nm="홍길동", age=18)) #이렇게도 사용 가능하다.

print(f"제 나이는 {age} 입니다.") #f-string 방식

print("제 나이는 %s 입니다." %age) #잘 나오기는 하지만 age는 정수이고 %s는 str이니 정수로 넣어도 문자열 형태로 포맷되서 들어간다.
print("제 나이는 %d 입니다." %age) # %d는 모든 문자를 정수형으로 포맷해서 출력
print("제 이름은 %s 이고, 제 나이는 %d 입니다." %(name, age)) #여러개도 사용 가능
print("Loading...%d%" %98) #이렇게 하면 에러가 뜨지만 %를 하나 더 써주면 된다. %d%%
print("%10s" % "hi") #앞에 공백이 생기는데 10칸 중 뒤에 hi채우고 앞에 공백을 채운다.그래서 공백은 hi가 두칸이니 8칸 공백이 생긴다.
#-10s로 해주면 hi가 앞에오고 뒤에 공백이 8칸 생긴다.
print("0.4d" % 3.422134) #앞의 0은 자리수를 의미 .4는 소수점 4번째 자리 까지 표현하라는 뜻

"""
#%s => 문자열
#%c => 문자 1개
#%d => 정수
#%f => 실수
#%o => 8진수
#%x => 16진수
#%% => 리터럴 (문자 % 제외)
#"""

#실습
#이름 :
#나이 :
#취미 :
#주소 :
#각각 변수에 넣고 f-string방식으로 출력하기
#ex) 제 이름은 ***이고 나이는 **살 입니다. 제 취미는 ***이고 주소는 ***입니다.

#name = "김영환"
#age = 29
#hobby = "game"
#address = "봉수로 270"
#print(f"제 이름은 {name} 이고 나이는 {age}살 입니다. 제 취미는 {hobby}이고 주소는 {address}입니다.")

name = input("이름 : ")
age = input("나이 : ")
hobby = input("취미 : ")
address = input("주소 : ")
print(f"제 이름은 {name} 이고 나이는 {age}살 입니다. 제 취미는 {hobby}이고 주소는 {address}입니다.")