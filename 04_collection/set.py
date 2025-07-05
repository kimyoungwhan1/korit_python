#세트
fruits = {"사과", "바나나", "오렌지", "바나나"} #중괄호로 감싸져있는 형태인데 딕셔너리는 키 벨류 형태고 얘는 요소만 들어가 있다.
print(fruits) #바나나가 한개만 나오는데 set라서 중복된 요소는 하나만 나옴, 순서가 없어서 자기 멋대로 순서가 다르다 실행시킬 때 마다
numbers = {1, 2, 3, 4, 5, 2, 3, 5}
print(numbers)

empty_set = {} #비어있는 딕셔너리 만들기
empty_dict = {} #비어있는 딕셔너리 만들기

empty_set = set() #비어있는 세트 만들기

#세트에 요소 추가하기
s = {1, 2, 3}
s.add(4) #요소 한개만 추가할 때
print(s)

s.update([5, 6, 7]) #여러개의 요소를 한번에 추가할 때
print(s)

#요소 삭제
s.remove(3)
print(s)
#함정이 있는데 만약 없는 값을 삭제할려고 시도하면 에러가 뜬다.
s.discard(9) #없는걸 제거할려고 시도해도 오류가 발생하지 않음
s.clear() #모두 삭제, 비어있는 세트가 출력 된다.

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A | B) #합집합으로 출력 된다. 중복제거 됨
print(A.union(B)) #합집합 방법

print(A & B) #교집합으로 출력
print(A.intersection(B))

print(A - B) #차집합으로 출력
print(A.difference(B))

#실습
python_class = {"철수", "영희", "민수", "지수"}
java_class = {"영희", "민수", "지훈", "길동"}
#파이썬과 자바 수업을 둘 다 듣는 사람 출력
#파이썬만 듣는 사람 출력
#자바만 듣는 사람 출력
print("둘 다 듣는 사람 :", python_class.intersection(java_class))
print("파이썬만 듣는 사람 :", python_class.difference(java_class))
print("자바만 듣는 사람 :", java_class.difference(python_class))

