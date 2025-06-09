from db_manager import *

if __name__ == '__main__':
    init_db()

    n = int(input("입력할 학생 수를 입력하세요: "))
    for _ in range(n):
        id = input("학번: ")
        name = input("이름: ")
        eng = int(input("영어 점수: "))
        c_lang = int(input("C-언어 점수: "))
        python = int(input("파이썬 점수: "))
        insert_student(id, name, eng, c_lang, python)

    print("\n전체 학생 정보:")
    print_all_students()

    print("\n80점 이상 학생 수:", count_above_80())

    keyword = input("\n검색할 학번 또는 이름 입력: ")
    results = search_student(keyword)
    print("검색 결과:", results)