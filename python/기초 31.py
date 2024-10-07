#리스트 평탄화 
def flatten(data):
    output = []
    for i in data:
        if type(i) == list:
            output = output + flatten(i) #한번 더 평탄화 시킴 
        else:
            output.append(i)
    return output

example = [[1,2,3],[4,[5,6]],7,[8,9]]
print(example)
print(flatten(example))
print()

#한 사람만 앉는 테이블이 없게 그룹 짓기
n = 2
c = 10
num = 100
memo = {}

def problem(a, b):
    key = str([a,b])

    if key in memo:
        return memo[key]
    if a < 0:
        return 0
    if a == 0:
        return 1
    output = 0
    for i in range(b, c + 1):
        output += problem(a - i, i)

    memo[key] = output

    return output

print(problem(num, n))
