#딕셔너리

profile = {
    "이름": "김영환",
    "나이": 29,
    "취미": ["여행", "게임"],
    2: 3,
    4: [1, 2, 3]#키는 문자열이 될 수도 있고 숫자가 될 수도 있다.
} #취미는 여러개니까 리스트 형태로 사용함

#요소 접근
print(profile["이름"])
print(profile["취미"][1]) #게임에 접근하기

#요소 수정
profile["나이"] = 28
print(profile)

#요소 추가
profile["직업"] = "강사"
print(profile) #수정이랑 추가가 똑같은데 나이라는 키가 이미 있으면 수정이 되는거고  키가 없으면 새로운 딕셔너리가 추가가 된다.

#요소 삭제
del profile["직업"]
print(profile)
profile.clear() #전체 삭제

#키만 불러오기, 어떤 키가 있는지 확인 가능
print(profile.keys())

#값만 불러오기
print(profile.values())

#키랑 값 둘다 불러오기
print(profile.items())

#새 딕셔너리 만들기
python_grade = {
    "kelly" : "B",
    "json" : "A",
    "ian" : "C",
    "elly" : "D"
}
print(sorted(python_grade.items())) #키 기준 오른차순으로 정렬하기
print(sorted(python_grade.items(), reverse=True)) #키 기준 내림차순으로 정렬하기

#실습
student = {}
#이름을 입력받고 해당 이름을 키로하고 점수를 입력받고 값으로 추가하기 student = {"김영환" : 80}이런 방식으로,
#input으로 점수를 받아서 "80"으로한다.
name = input("이름을 입력하세요 : ")
score = input(f"{name}의 점수를 입력하세요 : ")
student[name] = score
print(student)





