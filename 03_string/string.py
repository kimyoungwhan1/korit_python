#문자열의 인덱싱
a = "Life is too short, You need Python"
print(a[3]) #0, 1, 2, 3번 인덱스인 e가 출력된다.
print(a[-1]) #뒤에서 부터는 -1부터 시작한다.공백도 인덱스에 포함한다.

b = a[0] + a[1] + a[2] + a[3] #이렇게 인덱스를 뽑아서
print(b) #Life가 출력가능한다.

#실습
#단어를 입력받고 변수에 선언한 다음 첫 번째 글자와 마지막 글자를 출력하시오.
word= input("단어를 입력하세요 : ")
print("첫 번째 글자 -", word[0])
print("마지막 글자 -", word[-1])

#문자열의 슬라이싱
#문자열[start : end : step]
a = "Life is too short, You need Python"
print(a[0:4]) #Life가 나올것이다.
print(a[5:7]) #5번에서 7번 까지니까 is만 나올 것 이다. 끝 번호는 자기 자신을 포함하지 않는다.
print(a[19:]) #you need python만 출력하고 싶다면
print(a[:17]) #처음부터 17번 까지 출력하고 싶다면 처음생략하면 처음부터 끝번호 생략하면 끝번호 까지라는 뜻
print(a[19:-7]) #거꾸로 세는 인덱스
print(a[::2]) #스텝사용 처음부터 끝까지 인데 스텝이 2번, 첫 인덱스와 끝 인덱스를 를 생략했으니 처음부터 끝까지 인데 스텝을 2를
#줬으니까 2씩 더하면 되니 0인덱스, 2인덱스, 4인덱스 이런식으로 출력하게 된다.
print(a[::-1]) #문자열을 거꾸로 뒤집고 싶으면 스텝에 -1을 주면 된다.

#실습
date = "20250725unny"
#년도 출력
print("년도 : ", date[:4])
#월일 출력
print("월일: ", date[4:8])
#날씨 출력
print("날씨 : ", date[:])

a = "Life is too short, You need Python"
print(len(a)) #문자열의 길이 알기
print(a.count("t")) #t가 몇개 들어있는지 출력해줌
print(a.index("t")) #특정 문자의 인덱스 번호를 바로 알 수 있다. 이거는 3개중에 가장먼저 나온 t의 인덱스가 나올 것이다.
print(a.index("t", 10, 18))#두 번째나 세번째 인덱스 번호를 알고 싶을때 구간을 설정 할 수 있다.
##10번부터 18번 까지의 인덱스를 찾기위한 구간설정 (특정문자, 시작인덱스, 끝 인덱스)
print(a.find("t")) #인덱스랑 똑같은 일을 하는 하나가 더있다.
#find와 index의 차이점은 index는 해당문자가 없으면 오류를 발생시킨다. find는 -1을 반환한다.
print(",".join(a)) #문자 합치기 인데 사이 사이에 ,를 다 넣어준다.
print(a.upper()) #모두 대문자로 바꿔준다.
print(a.lower()) #모두 소문자로 바꿔준다.
print(a[0].isupper()) #a의 0번 인덱스는 대문자로 되어있다. 여기서 0번 인덱스의 대문자 여부를 묻는거다.
print(a[2].islower()) #2번 인덱스의 소문자 여부 출력

b = "       hi      "
print(b.lstrip()) #왼쪽 공백제거 해준다.
print(b.rstrip()) #오른쪽 공백제거
print(b.strip()) #양쪽 공백제거
print(a.replace("short", "long")) #short를 long로 바꿔준다.
print(a.replace(" ", "")) #사이사이에 공백들을 제거하기
print(a.split()) #아무것도 넣지 않으면 공백, 탭, 엔터 기준으로 나눔
c = "a:b:c:d"
print(c.split(":"))

#실습
#먼저 이메일을 입력받아서 변수에 저장, 해당 이메일에서 아이디만 출력하기
email = input("이메일을 입력하세요 : ")
print("이메일 아이디 : ", email[:email.index("@")]) #처음부터 @자리까지
print("이메일 아디디 : ", email.split("@")[0])
