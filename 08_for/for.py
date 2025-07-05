#반복문(for)
"""
for 변수 in 반복할 대상:
    반복할 코드
"""

#리스트 순회
fruits = ["사과", "바나나", "딸기", "포도"]

for fruit in fruits: #하나 씩 빼올 꺼니까 s뺀다
    print(fruit)

#딕셔너리 순회
scores = {
    "Alice" : 85,
    "Bob" : 92,
    "charlie" : 78
}
for key in scores: #키를 빼와서 변수에 할당한다.
    print(key, "의 점수는", scores[key])

#튜플 순회
a_tuple = ("안녕", "하세요", "반갑습니다.")
for a in a_tuple:
    print(a)

#set순회
a_set = {"사과", "바나나", "오렌지"}
for a in a_set:
    print(a)

#set정렬 추가 설명
numbers = {3, 1, 4, 5, 2, 6}
sorted_numbers = sorted(numbers)
print(sorted_numbers) #중복된거 사라지고 정렬된다.
print(type(sorted_numbers)) #세트를 넣어지만 리스트가 나온다.

