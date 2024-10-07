#재귀함수 팩토리얼 구하기
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

for i in range(4):
    print(factorial(i))
print()

#재귀함수  피보나치 수열1
def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(10))
print()

#재귀함수  피보나치 수열2
counter = 0

def fibonacci2(n):
    global counter
    counter += 1
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci2(n-1) + fibonacci2(n-2)

print(fibonacci2(10))
print(counter)
print()

#메모화
#메모 변수 생성
dict_a = {
    1: 1,
    2: 2
    }

def fibo(n):
    if n in dict_a:
        return dict_a[n]
    else:
        output = fibo(n-1) + fibo(n-2)
        dict_a[n] = output
        return output

print(fibo(10))
