#클래스 선언
class Student:
    count = 0
    students = []

    #클래스 함수
    @classmethod
    def print(cls):
        print("\t학생 목록\t")
        print("이름\t총점\t평균")
        for student in cls.students:
            print(str(student))
        print("----------------------")

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self)

    def get_sum(self):
        return self.korean+self.math+self.english+self.science
    
    def get_average(self):
        return self.get_sum()/4
    
    def __str__(self):
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_average())

#학생 리스트 선언
Student("윤인성", 87, 98, 88, 95)
Student("연하진", 92, 98, 96, 98)
Student("구지연", 76, 96, 94, 90)
Student("나선주", 98, 92, 96, 92)
Student("윤아린",95, 98, 98, 98)
Student("윤명월", 64, 88, 92, 92)

#학생 모두 출력
Student.print()
