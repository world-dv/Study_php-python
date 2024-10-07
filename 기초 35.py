#클래스 선언
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean+self.math+self.english+self.science

    def get_average(self):
        return self.get_sum()/4

    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average()
            )

#학생 리스트 선언
students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("존버는승리한다", 32, 91, 48, 62),
    Student("우루과이", 15, 99, 89, 49),
    Student("모히토", 100, 67, 82, 97),
    Student("케이크", 52, 38, 89, 59),
    Student("빵", 19, 35, 89, 94),
    Student("구름", 59, 64, 18, 93)
]

#출력
print("이름","총점","평균",sep="\t")
for student in students:
    print(str(student))
