import curses

import numpy as np

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
    curses.curs_set(0)
    stdscr.keypad(True)
    current = 0

    while True:
        stdscr.clear()
        stdscr.addstr(0, 2, "STUDENT MARK MANAGEMENT (PW4)", curses.A_BOLD)
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


def list_courses(courses):
    print("Danh sach mon hoc")
    if not courses:
        print("  (chua co mon hoc nao)")
    for c in courses:
        print(f"  {c.id} - {c.name} ({c.credit} tin chi)")
    print()


def list_students(students):
    print("Danh sach hoc sinh")
    if not students:
        print("  (chua co hoc sinh nao)")
    for s in students:
        print(f"  {s.id} - {s.name} - Sinh: {s.dob}")
    print()


def show_marks(students, courses):
    if not courses:
        print("Chua co mon hoc nao.")
        return
    list_courses(courses)
    cid = input("Nhap ma mon hoc muon xem diem: ").strip()
    course = next((c for c in courses if c.id == cid), None)
    if course is None:
        print(f"Khong tim thay mon hoc '{cid}'.")
        return
    print(f"Diem mon {course.name}")
    for s in students:
        mark = s.get_mark(cid)
        print(f"  {s.name} (ID {s.id}): {mark if mark is not None else 'Chua co diem'}")
    print()


def show_gpa_ranking(students, courses):
    if not students:
        print("Chua co hoc sinh nao.")
        return
    gpa_values = np.array([s.calculate_gpa(courses) or -1 for s in students])
    order = np.argsort(-gpa_values)  
    print("Bang xep hang GPA (giam dan)")
    for rank, i in enumerate(order, start=1):
        s = students[i]
        gpa = gpa_values[i]
        gpa_display = gpa if gpa != -1 else "Chua co diem"
        print(f"  #{rank}: {s.name} (ID {s.id}) - GPA: {gpa_display}")
    print()
