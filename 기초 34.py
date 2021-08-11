#학생 클래스 선언
class Student:
    def study(self):
        print("공부를 합니다.")

#선생님 클래스 선언
class Teacher:
    def teach(self):
        print("학생을 가르칩니다.")

#교실 내부의 객체 리스트를 생성
classroom = [Student(), Student(), Teacher(), Teacher(), Student(), Teacher()]

#반복을 통해 적절한 함수 호출
for person in classroom:
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()
