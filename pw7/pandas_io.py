import csv

import pandas as pd

STUDENTS_CSV = "students.csv"
COURSES_CSV = "courses.csv"
MARKS_CSV = "marks.csv"


def export_students_csv(students, filename=STUDENTS_CSV):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "dob"])
        for s in students:
            writer.writerow([s.id, s.name, s.dob])
    print(f"Da xuat '{filename}'")


def export_courses_csv(courses, filename=COURSES_CSV):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "credit"])
        for c in courses:
            writer.writerow([c.id, c.name, c.credit])
    print(f"Da xuat '{filename}'")


def export_marks_csv(students, filename=MARKS_CSV):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["course_id", "student_id", "mark"])
        for s in students:
            for cid, mark in s.marks.items():
                writer.writerow([cid, s.id, mark])
    print(f"Da xuat '{filename}'")


def export_all(students, courses):
    """Xuat ca 3 file CSV cung luc."""
    if not students:
        print("Chua co du lieu hoc sinh de xuat.")
        return
    export_students_csv(students)
    export_courses_csv(courses)
    export_marks_csv(students)
    print("Da xuat xong students.csv, courses.csv, marks.csv.\n")


def load_students_df(filename=STUDENTS_CSV):
    return pd.read_csv(filename)


def load_courses_df(filename=COURSES_CSV):
    return pd.read_csv(filename)


def load_marks_df(filename=MARKS_CSV):
    return pd.read_csv(filename)


def query_students(condition, filename=STUDENTS_CSV):
    """Chay 1 dieu kien kieu pandas .query() tren DataFrame students.
    Vi du dieu kien: name == "Alice"   hoac   dob == "01/01/2003" """
    df = load_students_df(filename)
    try:
        result = df.query(condition)
    except Exception as e:
        print(f"Dieu kien khong hop le: {e}")
        return None
    return result


def run_query_ui(students, courses):
    export_all(students, courses)

    print("Vi du dieu kien: name == 'Alice'")
    print("                  dob == '01/01/2003'")
    condition = input("Nhap dieu kien truy van: ").strip()
    if not condition:
        print("Dieu kien rong, huy truy van.")
        return

    result = query_students(condition)
    if result is None:
        return
    if result.empty:
        print("Khong tim thay ket qua phu hop.")
    else:
        print("Ket qua truy van")
        print(result)
