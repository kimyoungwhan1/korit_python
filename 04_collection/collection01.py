#List
from numpy.ma.core import product

fruits = ["apple", "banana", "cherry"] #대괄호로 감싸면 문자열 리스트
numbers = [1, 2, 3, 4, 5] #숫자 리스트
bools = [True, True, False, True, False] #불리언 리스트
mixed_list = ["안녕하세요", 42, 3.14, "ptthon", True] #혼합해서 사용이 가능하다.

#요소 접근 (인덱스)
print(fruits[0]) #apple이 나온다.
print(fruits[0][0]) #먼저 후르츠0번째인 apple 그리고 apple의 0번째인 a가 출력된다.
print(numbers[-1])

#요소 변경
fruits[1] = "blueberry"
print(fruits)

#요소 추가
fruits.append("grape") #마지막에 추가됨
fruits.insert(1, "mango") #원하는 인덱스 자리에 추가한다.
print(fruits)

#리스트 더하기
list1 = ["A", "B", "C"]
list2 = ["D", "E"]
print(list1 + list2)

#리스트 곱하기
print(list1 * 3)

#리스트에 여러 요소 추가하기
list1.extend(list2)
print(list1)

#요소 삭제
fruits.remove("cherry") #특정 값을 삭제하기
fruits.pop() #특정 인덱스로 삭제, 인덱스 생략시 마지막 요소를 삭제 한다. 하나 더 있다.
del fruits[2]
print(fruits)

#리스트 길이 구하기
print(len(fruits))

#리스트 슬라이싱
print(numbers[1:4]) #2에서 4까지 나온다.
print(numbers[::-1]) #문자열 뒤집힌다.

#리스트 정렬하기
numbers.sort() #기본적으로 오름차순으로 정렬된다.
print(numbers)
numbers.sort(reverse=True) #내림차순으로 정렬된다.
print(numbers)

list1.sort(reverse=True)
print(list1)

kor = ["가", "나", "다"]
kor.sort(reverse=True) #한글도 가능하다.
print(kor)

#원본에 영향을 주지않는 정렬
numbers2 = sorted(numbers) #새롭게 변수에 값을 할당한다.

#리스트 안에 요소가 존재하는지 체크
print("apple" in fruits) #부정으로 하고 싶으면 not in을 해주면 된다.

#리스트에 요소를 이어 붙이기
result = "-".join(list1)
print(result)


#리스트 실습
cart = []
#3개의 상품명을 입력 받아서 cart에 추가하기
# 최종적으로 cart를 출력

product1 = (input("추가할 상품 : "))
cart.append(product1)

product2 = (input("추가할 상품 : "))
cart.append(product2)

product3 = (input("추가할 상품 : "))
cart.append(product3)

print(cart)




#튜플
colors = ("red", "blue", "green")
numbers = (1, 2, 3, 4, 5)
mixed = ("pink", 1, True)
single_tuple = ("hello",) #요소를 하나만 넣고 싶으면 ,로 끝내줘야 한다.
alphabet =  ("a", "a", "a", "b", "c", "c")
#요소 접근
print(colors[1]) #블루가 나온다.

#요소 변경
colors[1] = "yellow" #튜플은 요소 변경이 불가능 하다.

#튜플 슬라이싱
print(colors[:2])
print(colors[::-1])

#count
print(alphabet.count("a"))

#index
print(alphabet.index("b")) #컬렉션 자료형 에서는 인덱스만 가능하고 find는 문자열에서만 가능하다.

#튜플 언패킹
a, b, c = colors #colors에 들어있는 순서대로 a, b, c에 red blue green이 들어가게 된다.
print(a, b, c)









