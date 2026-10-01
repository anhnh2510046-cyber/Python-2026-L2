import curses

import input as student_input     
import output as student_output   


def run(stdscr):
    students = []
    courses = []

    while True:
        choice = student_output.curses_menu(stdscr)

        # Thoat khoi curses de dung input()/print() binh thuong
        curses.endwin()

        if choice == 0:
            students = student_input.input_students()
        elif choice == 1:
            courses = student_input.input_courses()
        elif choice == 2:
            student_input.input_marks(students, courses)
        elif choice == 3:
            student_output.list_students(students)
        elif choice == 4:
            student_output.list_courses(courses)
        elif choice == 5:
            student_output.show_marks(students, courses)
        elif choice == 6:
            student_output.show_gpa_ranking(students, courses)
        elif choice == 7:
            print("Tam biet!")
            break

        input("\n(Nhan ENTER de quay lai menu...)")
        stdscr.refresh()  # quay lai che do curses


def main():
    curses.wrapper(run)


if __name__ == "__main__":
    main()
