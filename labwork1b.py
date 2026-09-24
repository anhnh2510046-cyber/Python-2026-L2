def input_students():
    students = []
    n = int(input("Nhap so luong hoc sinh: "))
    for i in range(n):
        print(f"-- Hoc sinh thu {i + 1} --")
        sid = input("  ID: ").strip()
        name = input("  Ho ten: ").strip()
        dob = input("  Ngay sinh (dd/mm/yyyy): ").strip()
        students.append({"id": sid, "name": name, "dob": dob})
    return students


def input_courses():
    courses = []
    n = int(input("Nhap so luong mon hoc: "))
    for i in range(n):
        print(f"-- Mon hoc thu {i + 1} --")
        cid = input("  Ma mon: ").strip()
        cname = input("  Ten mon: ").strip()
        courses.append({"id": cid, "name": cname})
    return courses


def input_marks(students, courses, marks):
    if not courses:
        print("Chua co mon hoc nao. Vui long them mon hoc truoc.")
        return
    if not students:
        print("Chua co hoc sinh nao. Vui long them hoc sinh truoc.")
        return

    list_courses(courses)
    cid = input("Nhap ma mon hoc can nhap diem: ").strip()
    course = find_course(courses, cid)
    if course is None:
        print(f"Khong tim thay mon hoc voi ma '{cid}'.")
        return

    course_marks = marks.get(cid, {})

    print(f"Nhap diem cho mon: {course['name']}")
    for s in students:
        while True:
            raw = input(f"  Diem cua {s['name']} (ID {s['id']}): ").strip()
            try:
                mark = float(raw)
                break
            except ValueError:
                print("  Diem khong hop le, vui long nhap lai (so).")
        course_marks[s["id"]] = mark

    marks[cid] = course_marks
    print("Da luu diem thanh cong!\n")

def list_courses(courses):
    print("Danh sach mon hoc")
    if not courses:
        print("  (chua co mon hoc nao)")
        return
    for c in courses:
        print(f"  {c['id']} - {c['name']}")
    print()


def list_students(students):
    print("Danh sach hoc sinh")
    if not students:
        print("  (chua co hoc sinh nao)")
        return
    for s in students:
        print(f"  {s['id']} - {s['name']} - Sinh: {s['dob']}")
    print()


def show_marks(students, courses, marks):
    if not courses:
        print("Chua co mon hoc nao.")
        return

    list_courses(courses)
    cid = input("Nhap ma mon hoc muon xem diem: ").strip()
    course = find_course(courses, cid)
    if course is None:
        print(f"Khong tim thay mon hoc voi ma '{cid}'.")
        return

    if cid not in marks:
        print(f"Mon {course['name']} chua co diem nao duoc nhap.\n")
        return

    print(f"Diem mon {course['name']}")
    for s in students:
        mark = marks[cid].get(s["id"], "Chua co diem")
        print(f"  {s['name']} (ID {s['id']}): {mark}")
    print()

def find_course(courses, cid):
    for c in courses:
        if c["id"] == cid:
            return c
    return None


def find_student(students, sid):
    for s in students:
        if s["id"] == sid:
            return s
    return None

MENU = """
1. Nhap thong tin hoc sinh
2. Nhap thong tin mon hoc
3. Nhap diem cho 1 mon hoc
4. Liet ke danh sach hoc sinh
5. Liet ke danh sach mon hoc
6. Xem diem hoc sinh theo mon
0. Thoat
"""


def main():
    students = []
    courses = []
    marks = {}

    while True:
        print(MENU)
        choice = input("Chon chuc nang: ").strip()

        if choice == "1":
            students = input_students()
        elif choice == "2":
            courses = input_courses()
        elif choice == "3":
            input_marks(students, courses, marks)
        elif choice == "4":
            list_students(students)
        elif choice == "5":
            list_courses(courses)
        elif choice == "6":
            show_marks(students, courses, marks)
        elif choice == "0":
            print("Tam biet!")
            break
        else:
            print("Lua chon khong hop le, vui long chon lai.\n")


if __name__ == "__main__":
    main()