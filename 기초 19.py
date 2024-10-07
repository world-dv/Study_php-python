#리스트 속 숫자 갯수 세기
numbers=[1,2,3,4,5,6,7,8,9,2,3,4,2,3,4]
counter={}

for number in numbers:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1

print(counter)
