# 학생 정보 입력 함수
def get_student_info():
    students = []
    for i in range(5):
        print(f"\n{i+1}번째 학생 정보 입력")
        student_id = input("학번: ")
        name = input("이름: ")
        english = int(input("영어: "))
        c_language = int(input("C-언어: "))
        python = int(input("파이썬: "))
        students.append({
            "student_id": student_id, 
            "name": name, 
            "english": english, 
            "c_language": c_language, 
            "python": python,
            "total": 0,
            "average": 0,
            "grade": "",
            "rank": 0
        })
    return students

# 총점 및 평균 계산 함수
def calculate_total_average(student):
    student["total"] = student["english"] + student["c_language"] + student["python"]
    student["average"] = student["total"] / 3

# 학점 계산 함수
def calculate_grade(student):
    avg = student["average"]
    if avg >= 90:
        student["grade"] = "A"
    elif avg >= 80:
        student["grade"] = "B"
    elif avg >= 70:
        student["grade"] = "C"
    elif avg >= 60:
        student["grade"] = "D"
    else:
        student["grade"] = "F"

# 등수 계산 함수
def calculate_rank(students):
    students.sort(key=lambda x: x["total"], reverse=True)
    rank = 1
    prev_total = -1
    for i, student in enumerate(students):
        if student["total"] != prev_total:
            rank = i + 1
        student["rank"] = rank
        prev_total = student["total"]

# 출력 함수
def display_results(students):
    print("\n{:^90}".format("성적관리 프로그램"))
    print("=" * 90)
    print("{:<12}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}{:<6}{:<6}".format(
        "학번", "이름", "영어", "C-언어", "파이썬", "총점", "평균", "학점", "등수"))
    print("=" * 90)
    for student in students:
        print("{:<12}{:<8}{:>8}{:>8}{:>8}{:>8}{:>8.2f}{:>6}{:>6}".format(
            student["student_id"], student["name"], student["english"], student["c_language"], student["python"],
            student["total"], student["average"], student["grade"], student["rank"]))
    print("=" * 90)


students = get_student_info()
for student in students:
    calculate_total_average(student)
    calculate_grade(student)
calculate_rank(students)
display_results(students)

