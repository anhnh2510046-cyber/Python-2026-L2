import os
import zipfile

from domains import Student, Course

STUDENTS_FILE = "students.txt"
COURSES_FILE = "courses.txt"
MARKS_FILE = "marks.txt"
ARCHIVE_NAME = "students.dat"

DATA_FILES = [STUDENTS_FILE, COURSES_FILE, MARKS_FILE]

COMPRESSION_METHODS = {
    "1": ("STORED (khong nen)", zipfile.ZIP_STORED),
    "2": ("DEFLATED (nen mac dinh, pho bien)", zipfile.ZIP_DEFLATED),
    "3": ("BZIP2 (nen manh hon, cham hon)", zipfile.ZIP_BZIP2),
    "4": ("LZMA (nen manh nhat, cham nhat)", zipfile.ZIP_LZMA),
}


def write_students_file(students, filename=STUDENTS_FILE):
    with open(filename, "w", encoding="utf-8") as f:
        for s in students:
            f.write(f"{s.id}|{s.name}|{s.dob}\n")
    print(f"Da ghi thong tin hoc sinh vao '{filename}'")


def write_courses_file(courses, filename=COURSES_FILE):
    with open(filename, "w", encoding="utf-8") as f:
        for c in courses:
            f.write(f"{c.id}|{c.name}|{c.credit}\n")
    print(f"Da ghi thong tin mon hoc vao '{filename}'")


def write_marks_file(students, filename=MARKS_FILE):
    with open(filename, "w", encoding="utf-8") as f:
        for s in students:
            for cid, mark in s.marks.items():
                f.write(f"{cid}|{s.id}|{mark}\n")
    print(f"Da ghi diem vao '{filename}'")


def load_students(filename=STUDENTS_FILE):
    students = []
    if not os.path.exists(filename):
        return students
    with open(filename, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            sid, name, dob = line.split("|")
            students.append(Student(sid, name, dob))
    return students


def load_courses(filename=COURSES_FILE):
    courses = []
    if not os.path.exists(filename):
        return courses
    with open(filename, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            cid, cname, credit = line.split("|")
            courses.append(Course(cid, cname, int(credit)))
    return courses


def load_marks(students, filename=MARKS_FILE):
    if not os.path.exists(filename):
        return
    student_map = {s.id: s for s in students}
    with open(filename, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            cid, sid, mark = line.split("|")
            if sid in student_map:
                student_map[sid].set_mark(cid, float(mark))


def load_all():
    students = load_students()
    courses = load_courses()
    load_marks(students)
    return students, courses


def select_compression_method():
    print("Chon phuong phap nen du lieu:")
    for key, (label, _) in COMPRESSION_METHODS.items():
        print(f"  {key}. {label}")
    choice = input("Nhap lua chon (Enter = mac dinh DEFLATED): ").strip() or "2"
    if choice not in COMPRESSION_METHODS:
        print("Lua chon khong hop le, dung DEFLATED mac dinh.")
        choice = "2"
    return COMPRESSION_METHODS[choice][1]


def compress_data(method=None, archive_name=ARCHIVE_NAME):
    if method is None:
        method = select_compression_method()
    with zipfile.ZipFile(archive_name, "w") as zf:
        for filename in DATA_FILES:
            if os.path.exists(filename):
                zf.write(filename, arcname=filename, compress_type=method)
    print(f"Da nen du lieu vao '{archive_name}'")


def data_exists(archive_name=ARCHIVE_NAME):
    return os.path.exists(archive_name)


def decompress_data(archive_name=ARCHIVE_NAME):
    with zipfile.ZipFile(archive_name, "r") as zf:
        zf.extractall(".")
    print(f"Da giai nen du lieu tu '{archive_name}'")
