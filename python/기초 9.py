#날짜/시간과 관련된 기능을 가져옵니다.
import datetime

#현재 날짜/시간을 구합니다.
now = datetime.datetime.now()

#출력
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")

#한줄로 출력하기
print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
    ))

#오전 구분
if now.hour < 12:
    print("현재 시간은 {}시로 오전입니다.".format(now.hour))

#오후 구분
if now.hour >= 12:
    print("현재 시간은 {}시로 오후입니다.".format(now.hour))

#봄 구분
if 3 <= now.month <= 5:
    print("봄")

#여름 구분
if 6 <= now.month <= 8:
    print("여름")

#가을 구분
if 9 <= now.month <= 11:
    print("가을")

#겨울 구분
if 12 <= now.month <= 2:
    print("겨울")
