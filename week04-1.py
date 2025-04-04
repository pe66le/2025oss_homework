class Student:
    def __init__(self, student_id, name, english, c_lang, python):
        self.student_id = student_id
        self.name = name
        self.english = english
        self.c_lang = c_lang
        self.python = python
        self.total = self.calculate_total()
        self.average = self.calculate_average()
        self.grade = self.calculate_grade()
        self.rank = 0  # 초기값, 이후 계산

    def calculate_total(self):
        return self.english + self.c_lang + self.python

    def calculate_average(self):
        return self.total / 3

    def calculate_grade(self):
        if self.average >= 90:
            return "A"
        elif self.average >= 80:
            return "B"
        elif self.average >= 70:
            return "C"
        elif self.average >= 60:
            return "D"
        else:
            return "F"

def input_students():
    students = []
    for _ in range(5):  # 5명의 학생 입력
        student_id = input("학번: ")
        name = input("이름: ")
        english = int(input("영어 점수: "))
        c_lang = int(input("C-언어 점수: "))
        python = int(input("파이썬 점수: "))
        students.append(Student(student_id, name, english, c_lang, python))
    return students

def print_students(students):
    print("\n=== 학생 성적 목록 ===")
    print(f"{'학번':<10}{'이름':<10}{'영어':<6}{'C-언어':<6}{'파이썬':<6}{'총점':<6}{'평균':<8}{'학점':<4}")
    for s in students:
        print(f"{s.student_id:<10}{s.name:<10}{s.english:<6}{s.c_lang:<6}{s.python:<6}{s.total:<6}{s.average:<8.2f}{s.grade:<4}")

students = input_students()
print_students(students)
