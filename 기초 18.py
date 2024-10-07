#딕셔너리 생성
dict_a = {
    "name":"건조 망고",
    "type":"당절임",
    "ingredient":["망고","설탕","메타중아황산나트륨","치자황색소"],
    "origin":"필리핀"
    }

#값 출력
print(dict_a["name"])
print(dict_a["type"])
print(dict_a["ingredient"])
print(dict_a["origin"])
print()

#값 바꾸기
dict_a["name"] = "건 망고"
print(dict_a["name"])

#값에 접근
key=input(">접근하고자 하는 키>")

if key in dict_a:
    print(dict_a[key])
else:
    print("존재 하지 않음")

#키가 존재 하지 않을 때 NONE 출력하는 지 확인하기
print()
value=dict_a.get("존재하지 않는 키")
print("값 :", value)

if value == None:
    print("존재 하지 않는 키 입니다.")

#반복문을 이용해 출력
print()
for key in dict_a:
    print(dict_a[key])
