##############################
# 프로그램명: score_manager.py
# 작성자: 소프트웨어학부/한정우
# 작성일: 2025-04-13
# 프로그램 설명:
#   5명의 학생에 대해 학번, 이름, 영어, C-언어, 파이썬 점수를 입력
#   총점, 평균, 학점, 등수를 계산하고 관리하는 "객체지향" 성적 관리 프로그램
#   추가적으로, 학생 정보의 삽입, 삭제, 탐색(학번 및 이름),
#   총점 기준 정렬(내림차순) 및 평균 80점 이상인 학생 수 카운트 기능
##############################

class Student:
    def __init__(self, stu_id, name, english, c_lang, python_score):
        self.stu_id = stu_id            # 학번
        self.name = name                # 이름
        self.english = english          # 영어 점수
        self.c_lang = c_lang            # C-언어 점수
        self.python_score = python_score  # 파이썬 점수
        self.total = 0                  # 총점 
        self.avg = 0.0                  # 평균 
        self.grade = ''                 # 학점 
        self.rank = 1                   # 등수 

    def calc_total_and_avg(self):
        """영어, C-언어, 파이썬 점수를 합산하여 총점과 평균을 계산한다."""
        self.total = self.english + self.c_lang + self.python_score
        self.avg = self.total / 3

    def calc_grade(self):
        """평균 점수를 기준으로 학점을 계산한다."""
        if self.avg >= 90:
            self.grade = 'A'
        elif self.avg >= 80:
            self.grade = 'B'
        elif self.avg >= 70:
            self.grade = 'C'
        elif self.avg >= 60:
            self.grade = 'D'
        else:
            self.grade = 'F'

    def update(self):
        """총점, 평균, 학점을 갱신한다."""
        self.calc_total_and_avg()
        self.calc_grade()

    def __str__(self):
        """학생 정보를 정렬된 형식의 문자열로 반환한다."""
        return (f"{self.stu_id:10} {self.name:10} {self.english:8} {self.c_lang:8} "
                f"{self.python_score:8} {self.total:8} {self.avg:8.2f} "
                f"{self.grade:6} {self.rank:6}")


class StudentManager:
    def __init__(self):
        self.students = []  

    def input_students(self, count=5):
        """사용자로부터 학생 정보를 입력받아 객체를 생성하고 리스트에 추가한다."""
        print(f"\n학생 {count}명의 정보를 입력하세요.")
        for i in range(count):
            print(f"\n학생 #{i+1}")
            stu_id = input("학번: ")
            name = input("이름: ")
            try:
                english = int(input("영어 점수: "))
                c_lang = int(input("C-언어 점수: "))
                python_score = int(input("파이썬 점수: "))
            except ValueError:
                print("잘못된 입력입니다. 정수형 숫자를 입력해주세요.")
                continue

            student = Student(stu_id, name, english, c_lang, python_score)
            student.update()
            self.students.append(student)
        self.calculate_ranks()

    def display_students(self):
        """현재 저장된 모든 학생 정보를 출력한다."""
        if not self.students:
            print("입력된 학생이 없습니다.")
            return

        header = (f"{'학번':10} {'이름':10} {'영어':8} {'C-언어':8} {'파이썬':8} "
                  f"{'총점':8} {'평균':8} {'학점':6} {'등수':6}")
        print("\n학생 정보 목록")
        print(header)
        print("-" * len(header))
        for student in self.students:
            print(student)

    def calculate_ranks(self): # 총점을 비교하여 등수를 산출
        for s in self.students:
            s.rank = 1
        for i in range(len(self.students)):
            for j in range(len(self.students)):
                if self.students[j].total > self.students[i].total:
                    self.students[i].rank += 1

    def insert_student(self): # 새로운 학생 정보를 입력받아 리스트에 추가
        print("\n새로운 학생 정보를 입력합니다.")
        stu_id = input("학번: ")
        name = input("이름: ")
        try:
            english = int(input("영어 점수: "))
            c_lang = int(input("C-언어 점수: "))
            python_score = int(input("파이썬 점수: "))
        except ValueError:
            print("잘못된 입력입니다. 정수형 숫자를 입력해주세요.")
            return

        student = Student(stu_id, name, english, c_lang, python_score)
        student.update()
        self.students.append(student)
        self.calculate_ranks()
        print("학생 정보가 추가되었습니다.")

    def delete_student(self): # 특정 학번의 학생 정보를 삭제
        stu_id = input("삭제할 학생의 학번을 입력하세요: ")
        for i, student in enumerate(self.students):
            if student.stu_id == stu_id:
                del self.students[i]
                self.calculate_ranks()
                print("학생 정보가 삭제되었습니다.")
                return
        print("해당 학번의 학생을 찾을 수 없습니다.")

    def search_student_by_id(self): # 학번을 기준으로 학생 정보를 탐색하여 출력
        stu_id = input("검색할 학생의 학번을 입력하세요: ")
        found = False
        for student in self.students:
            if student.stu_id == stu_id:
                print("\n검색 결과:")
                header = (f"{'학번':10} {'이름':10} {'영어':8} {'C-언어':8} "
                          f"{'파이썬':8} {'총점':8} {'평균':8} {'학점':6} {'등수':6}")
                print(header)
                print("-" * len(header))
                print(student)
                found = True
                break
        if not found:
            print("해당 학번의 학생을 찾을 수 없습니다.")

    def search_student_by_name(self): # 이름을 기준으로 학생 정보를 탐색하여 출력
        name = input("검색할 학생의 이름을 입력하세요: ")
        found_students = [student for student in self.students if student.name == name]
        if found_students:
            print("\n검색 결과:")
            header = (f"{'학번':10} {'이름':10} {'영어':8} {'C-언어':8} "
                      f"{'파이썬':8} {'총점':8} {'평균':8} {'학점':6} {'등수':6}")
            print(header)
            print("-" * len(header))
            for student in found_students:
                print(student)
        else:
            print("해당 이름의 학생을 찾을 수 없습니다.")

    def sort_by_total(self): # 총점 기준 내림차순으로 정렬
        self.students.sort(key=lambda s: s.total, reverse=True)
        self.calculate_ranks()
        print("총점 기준 내림차순으로 정렬하였습니다.")

    def count_above_80(self): # 평균 80점 이상인 학생의 수를 카운트하여 출력
        count = sum(1 for s in self.students if s.avg >= 80)
        print(f"평균 80점 이상인 학생 수: {count}")


def main():
    manager = StudentManager()
    
    while True:
        print("\n========== 성적 관리 프로그램 ==========")
        print("1. 학생 정보 입력 (5명)")
        print("2. 학생 정보 출력")
        print("3. 학생 정보 삽입")
        print("4. 학생 정보 삭제")
        print("5. 학생 정보 탐색 (학번)")
        print("6. 학생 정보 탐색 (이름)")
        print("7. 총점 기준 정렬 (내림차순)")
        print("8. 평균 80점 이상 학생 수 카운트")
        print("0. 종료")
        choice = input("원하는 메뉴 번호를 입력하세요: ")

        if choice == '1':
            manager.input_students(5)
        elif choice == '2':
            manager.display_students()
        elif choice == '3':
            manager.insert_student()
        elif choice == '4':
            manager.delete_student()
        elif choice == '5':
            manager.search_student_by_id()
        elif choice == '6':
            manager.search_student_by_name()
        elif choice == '7':
            manager.sort_by_total()
        elif choice == '8':
            manager.count_above_80()
        elif choice == '0':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")


if __name__ == '__main__':
    main()
