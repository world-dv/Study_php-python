#학생 리스트 선언
students = [
    { "name":"윤인성", "Korean":87,"math":98,"english":88,"science":95},
    { "name":"나비", "Korean":25,"math":42,"english":25,"science":87},
    { "name":"고양이", "Korean":81,"math":73,"english":84,"science":100},
    { "name":"바질", "Korean":90,"math":86,"english":32,"science":57},
    { "name":"아이", "Korean":82,"math":92,"english":85,"science":29},
    { "name":"집", "Korean":56,"math":68,"english":58,"science":90}
    ]

#학생을 한 명씩 반복
print("이름","총점","평균",sep='\t')

for student in students:
    score_sum = student["Korean"]+student["math"]+student["english"]\
                +student["science"]
    score_average = score_sum / 4
    print(student["name"], score_sum, score_average, sep='\t')
print()

#딕셔너리를 리턴하는 함수 선언
def create_student(name, korean, math, english, science):
    return {
        "name" : name,
        "korean" : korean,
        "math" : math,
        "english" : english,
        "science" : science
        }

students = [
    create_student("윤인성", 87, 98, 88, 95),
    create_student("존버는승리한다", 32, 91, 48, 62),
    create_student("우루과이", 15, 99, 89, 49),
    create_student("모히토", 100, 67, 82, 97),
    create_student("케이크", 52, 38, 89, 59),
    create_student("빵", 19, 35, 89, 94),
    create_student("구름", 59, 64, 18, 93)
    ]

#학생을 한 명씩 반복
print("이름","총점","평균",sep='\t')

for student in students:
    score_sum = student["korean"]+student["math"]+student["english"]\
                +student["science"]
    score_average = score_sum / 4
    print(student["name"], score_sum, score_average, sep='\t')
print()

#학생 처리 함수 선언
def student_sum(student):
    return  student["korean"]+student["math"]+student["english"]\
                +student["science"]
def student_average(student):
    return student_sum(student) / 4
def student_print(student):
    return "{}\t{}\t{}".format(student["name"], student_sum(student), student_average(student))

#학생을 한 명씩 반복
print("이름","총점","평균",sep='\t')
for student in students:
    print(student_print(student))
