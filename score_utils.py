def compute_scores(eng, c_lang, python):
    total = eng + c_lang + python
    avg = total / 3
    grade = (
        'A' if avg >= 90 else
        'B' if avg >= 80 else
        'C' if avg >= 70 else
        'D' if avg >= 60 else
        'F'
    )
    return total, avg, grade
