#자료형 확인하기
character = {
    "name":"기사",
    "level":12,
    "items":{
        "sword":"불꽃의 검",
        "armor":"폼플레이트"
        },
    "skill":["베기","세게 베기","아주 세게 베기"]
    }


for key in character:
    if type(character[key]) == dict:
        for i in character[key]:
            print(i,":",character[key][i])
    elif type(character[key]) == list:
        for i in character[key]:
            print(key,":",i)
    else:
        print(key,":",character[key])
