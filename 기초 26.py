#리스트 내포
array = [ i*i for i in range(0,20,2)]
print(array)

#조건 활용
output = [ i for i in array if i != 144]
print(output)

#join 함수
for i in array:
    if i % 2 == 0:
        print("\n".join([
            "입력한 문자열은 {}입니다."
            "{}는(은) 짝수입니다."
            ]).format(i,i))
    else:
        print("\n".join([
            "입력한 문자열은 {}입니다."
            "{}는(은) 홀수입니다."
            ]).format(i,i))
