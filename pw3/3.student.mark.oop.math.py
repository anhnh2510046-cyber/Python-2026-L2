import math
import numpy as np
import curses

def floor_to_1_decimal(x):
    return math.floor(x * 10) / 10

def input_students():
    students = []
    n = int(input("Nhap so luong hoc sinh: "))
    for i in range(n):
        print(f"Hoc sinh thu {i + 1}")
        sid = input("  ID: ").strip()
        name = input("  Ho ten: ").strip()
        dob = input("  Ngay sinh (dd/mm/yyyy): ").strip()
        students.append({"id": sid, "name": name, "dob": dob})
    return students

def input_courses():
    courses = []
    n = int(input("Nhap so luong mon hoc: "))
    for i in range(n):
        print(f"Mon hoc thu {i + 1}")
        cid = input("  Ma mon: ").strip()
        cname = input("  Ten mon: ").strip()
        credit = int(input("  So tin chi: ").strip())
        courses.append({"id": cid, "name": cname, "credit": credit})
    return courses

def input_marks(students, courses, marks):
    if not courses or not students:
        print("Can co du hoc sinh va mon hoc truoc khi nhap diem.")
        return

    list_courses(courses)
    cid = input("Nhap ma mon hoc can nhap diem: ").strip()
    course = find_course(courses, cid)
    if course is None:
        print(f"Khong tim thay mon hoc '{cid}'.")
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
                print("  Diem khong hop le, nhap lai.")
        course_marks[s["id"]] = floor_to_1_decimal(mark)

    marks[cid] = course_marks
    print("Da luu diem!\n")

def calculate_gpa(sid, courses, marks):
    score_list = []
    credit_list = []
    for c in courses:
        cid = c["id"]
        if cid in marks and sid in marks[cid]:
            score_list.append(marks[cid][sid])
            credit_list.append(c["credit"])

    if not credit_list:
        return None

    scores = np.array(score_list, dtype=float)
    credits = np.array(credit_list, dtype=float)
    gpa = np.sum(scores * credits) / np.sum(credits)
    return round(float(gpa), 2)

def sort_students_by_gpa_desc(students, courses, marks):
    gpa_values = np.array([
        calculate_gpa(s["id"], courses, marks) or -1  # None -> xep cuoi
        for s in students
    ])
    order = np.argsort(-gpa_values)
    sorted_students = [students[i] for i in order]
    sorted_gpas = gpa_values[order]
    return sorted_students, sorted_gpas

def list_courses(courses):
    print("Danh sach mon hoc")
    if not courses:
        print("  (chua co mon hoc nao)")
    for c in courses:
        print(f"  {c['id']} - {c['name']} ({c['credit']} tin chi)")
    print()


def list_students(students):
    print("Danh sach hoc sinh")
    if not students:
        print("  (chua co hoc sinh nao)")
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
        print(f"Khong tim thay mon hoc '{cid}'.")
        return
    if cid not in marks:
        print(f"Mon {course['name']} chua co diem.\n")
        return
    print(f"Diem mon {course['name']}")
    for s in students:
        mark = marks[cid].get(s["id"], "Chua co diem")
        print(f"  {s['name']} (ID {s['id']}): {mark}")
    print()


def show_gpa_ranking(students, courses, marks):
    if not students:
        print("Chua co hoc sinh nao.")
        return
    sorted_students, sorted_gpas = sort_students_by_gpa_desc(students, courses, marks)
    print("Bang xep hang GPA")
    for rank, (s, gpa) in enumerate(zip(sorted_students, sorted_gpas), start=1):
        gpa_display = gpa if gpa != -1 else "Chua co diem"
        print(f"  #{rank}: {s['name']} (ID {s['id']}) - GPA: {gpa_display}")
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

MENU_OPTIONS = [
    "Nhap thong tin hoc sinh",
    "Nhap thong tin mon hoc",
    "Nhap diem cho 1 mon hoc",
    "Liet ke danh sach hoc sinh",
    "Liet ke danh sach mon hoc",
    "Xem diem hoc sinh theo mon",
    "Xem bang xep hang GPA",
    "Thoat",
]

def curses_menu(stdscr):
    curses.curs_set(0)          # an con tro nhap
    stdscr.keypad(True)         # cho phep nhan phim mui ten
    current = 0

    while True:
        stdscr.clear()
        stdscr.addstr(0, 2, "STUDENT MARK MANAGEMENT (PW3)", curses.A_BOLD)
        for idx, option in enumerate(MENU_OPTIONS):
            y = idx + 2
            if idx == current:
                stdscr.attron(curses.A_REVERSE)
                stdscr.addstr(y, 4, f"> {option}")
                stdscr.attroff(curses.A_REVERSE)
            else:
                stdscr.addstr(y, 4, f"  {option}")
        stdscr.addstr(len(MENU_OPTIONS) + 3, 2, "Dieu huong: UP/DOWN, chon: ENTER")
        stdscr.refresh()

        key = stdscr.getch()
        if key == curses.KEY_UP:
            current = (current - 1) % len(MENU_OPTIONS)
        elif key == curses.KEY_DOWN:
            current = (current + 1) % len(MENU_OPTIONS)
        elif key in (curses.KEY_ENTER, 10, 13):
            return current

def run(stdscr):
    students = []
    courses = []
    marks = {}

    while True:
        choice = curses_menu(stdscr)

        # Thoat khoi curses de dung input()/print()
        curses.endwin()

        if choice == 0:
            students = input_students()
        elif choice == 1:
            courses = input_courses()
        elif choice == 2:
            input_marks(students, courses, marks)
        elif choice == 3:
            list_students(students)
        elif choice == 4:
            list_courses(courses)
        elif choice == 5:
            show_marks(students, courses, marks)
        elif choice == 6:
            show_gpa_ranking(students, courses, marks)
        elif choice == 7:
            print("Tam biet!")
            break

        input("\n(Nhan ENTER de quay lai menu...)")
        stdscr.refresh()  # quay lai che do curses


def main():
    curses.wrapper(run)


if __name__ == "__main__":
    main()
