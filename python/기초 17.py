numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    if number % 2 == 0:
        print(number, "는 짝수입니다.")
    elif number % 2 == 1:
        print(number, "는 홀수입니다.")

for number in numbers:
    print(number, "는", len(str(number)), "자릿수입니다.")

list_of_list = [
    [1,2,3],
    [4,5,6,7],
    [8,9],
    ]

for list in list_of_list:
    for element in list:
        print(element)


numbers = [1,2,3,4,5,6,7,8,9]
output =[[],[],[]]

for number in numbers:
    output[(number+2)%3].append(number)

print(output)
    
