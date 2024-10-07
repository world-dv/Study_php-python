example_list = ["요소1","요소2","요소3"]

#enumerate()함수 적용 출력
print(enumerate(example_list))
print()

#list() 함수로 강제 변환 출력
print(list(enumerate(example_list)))

#반복문과 조합
for i, value in enumerate(example_list):
    print(i, ":", value)
print()


example_list = {
    "A" : "요소1",
    "B" : "요소2",
    "C" : "요소3"
    }

#items()함수
print(example_list.items())


for key, element in example_list.items():
    print(key, element)
    
