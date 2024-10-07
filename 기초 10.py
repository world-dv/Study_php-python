#입력
number = input("입력 > ")

#마지막 숫자 추출
last_charachter = number[-1]

#숫자로 변환
last_number = int(last_charachter)

#짝수 확인
if last_number % 2 == 0:
                  print("짝수")

if last_number == 0\
   or last_number == 2\
   or last_number == 4\
   or last_number == 6\
   or last_number == 8:
    print("짝짝수")

#홀수 확인
if last_number % 2 == 1:
    print("홀수")

if last_number == 1\
   or last_number == 3\
   or last_number == 5\
   or last_number == 7\
   or last_number == 9:
    print("홀홀수")

#짝수 조건
if last_charachter in "02468":
    print("짝수짝수짝짝")

#홀수 조건
if last_charachter in "13579":
    print("홀수홀수홀홀")
