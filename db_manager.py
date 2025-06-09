import sqlite3
from score_utils import compute_scores

def init_db():
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS grades (
            id TEXT PRIMARY KEY,
            name TEXT,
            eng INTEGER,
            c_lang INTEGER,
            python INTEGER,
            total INTEGER,
            average REAL,
            grade TEXT,
            rank INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def reset_db():
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS grades")
    conn.commit()
    conn.close()
    init_db()
    print("[✓] 데이터베이스가 초기화되었습니다.")

def insert_student(id, name, eng, c_lang, python):
    total, avg, grade = compute_scores(eng, c_lang, python)
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()

    # 먼저 학번 중복 확인
    cur.execute("SELECT id FROM grades WHERE id = ?", (id,))
    if cur.fetchone():
        print(f"[!] 학번 {id} 는 이미 존재합니다. 삽입하지 않습니다.")
        conn.close()
        return

    cur.execute('''
        INSERT INTO grades (id, name, eng, c_lang, python, total, average, grade)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (id, name, eng, c_lang, python, total, avg, grade))
    conn.commit()
    conn.close()

def delete_student(id):
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM grades WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def search_student(keyword):
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM grades WHERE id = ? OR name = ?", (keyword, keyword))
    results = cur.fetchall()
    conn.close()
    return results

def sort_students_by_total():
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM grades ORDER BY total DESC")
    results = cur.fetchall()
    conn.close()
    return results

def count_above_80():
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM grades WHERE eng >= 80 AND c_lang >= 80 AND python >= 80")
    count = cur.fetchone()[0]
    conn.close()
    return count

def update_ranks():
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("SELECT id FROM grades ORDER BY total DESC")
    ids = cur.fetchall()
    for rank, (id,) in enumerate(ids, start=1):
        cur.execute("UPDATE grades SET rank = ? WHERE id = ?", (rank, id))
    conn.commit()
    conn.close()

def print_all_students():
    update_ranks()
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM grades ORDER BY rank ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.close()