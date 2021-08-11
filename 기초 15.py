#리스트 선언
list_a = [1, 2, 3]

#요소 추가
print("#리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)
print(list_a)
print()

#리스트 중간에 요소 추가
print("리스트 중간에 요소 추가")
list_a.insert(0, 10)
print(list_a)

#인덱스 제거
del list_a[0]
print(list_a)

list_a.pop(3)
print(list_a)

#리스트 초기화
list_a.clear()
print(list_a)
