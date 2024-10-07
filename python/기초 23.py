#변수 선언
list_test=[1,2,3,4,1]
value = 1

#리스트에 해당하는 값 모두 제거
while value in list_test:
    list_test.remove(value)

print(list_test)
