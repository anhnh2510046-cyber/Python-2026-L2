import curses

import input as student_input
import output as student_output
import storage
import pandas_io


def run(stdscr, students, courses):
    while True:
        choice = student_output.curses_menu(stdscr)

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
            pandas_io.export_all(students, courses)
        elif choice == 8:
            pandas_io.run_query_ui(students, courses)
        elif choice == 9:
            storage.save_pickle(students, courses)
            loaded_students, loaded_courses = storage.load_pickle()
            print(
                f"Doc lai tu pickle: {len(loaded_students)} hoc sinh, "
                f"{len(loaded_courses)} mon hoc."
            )
        elif choice == 10:
            print("Dang luu du lieu truoc khi thoat...")
            method = storage.select_compression_method()
            storage.compress_data(method)
            print("Tam biet!")
            break

        input("\n(Nhan ENTER de quay lai menu...)")
        stdscr.refresh()


def main():
    students = []
    courses = []

    if storage.data_exists():
        print(f"Phat hien file '{storage.ARCHIVE_NAME}', dang giai nen va tai du lieu...")
        storage.decompress_data()
        students, courses = storage.load_all()
        print(f"Da tai {len(students)} hoc sinh, {len(courses)} mon hoc tu lan truoc.")
        input("Nhan ENTER de vao chuong trinh...")

    curses.wrapper(lambda stdscr: run(stdscr, students, courses))


if __name__ == "__main__":
    main()
