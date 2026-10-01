import math

from domains import Student, Course


def floor_to_1_decimal(x):
    return math.floor(x * 10) / 10


def input_students():
    students = []
    n = int(input("Nhap so luong hoc sinh: "))
    for i in range(n):
        print(f"-- Hoc sinh thu {i + 1} --")
        sid = input("  ID: ").strip()
        name = input("  Ho ten: ").strip()
        dob = input("  Ngay sinh (dd/mm/yyyy): ").strip()
        students.append(Student(sid, name, dob))
    return students


def input_courses():
    courses = []
    n = int(input("Nhap so luong mon hoc: "))
    for i in range(n):
        print(f"-- Mon hoc thu {i + 1} --")
        cid = input("  Ma mon: ").strip()
        cname = input("  Ten mon: ").strip()
        credit = int(input("  So tin chi: ").strip())
        courses.append(Course(cid, cname, credit))
    return courses


def input_marks(students, courses):
    if not courses or not students:
        print("Can co du hoc sinh va mon hoc truoc khi nhap diem.")
        return

    for c in courses:
        print(f"  {c.id} - {c.name} ({c.credit} tin chi)")
    cid = input("Nhap ma mon hoc can nhap diem: ").strip()
    course = next((c for c in courses if c.id == cid), None)
    if course is None:
        print(f"Khong tim thay mon hoc '{cid}'.")
        return

    print(f"Nhap diem cho mon: {course.name}")
    for s in students:
        while True:
            raw = input(f"  Diem cua {s.name} (ID {s.id}): ").strip()
            try:
                mark = float(raw)
                break
            except ValueError:
                print("  Diem khong hop le, nhap lai.")
        s.set_mark(cid, floor_to_1_decimal(mark))

    print("Da luu diem!\n")
