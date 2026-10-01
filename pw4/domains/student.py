import numpy as np

class Student:
    def __init__(self, sid, name, dob):
        self.id = sid
        self.name = name
        self.dob = dob
        self.marks = {}   

    def set_mark(self, course_id, mark):
        self.marks[course_id] = mark

    def get_mark(self, course_id):
        return self.marks.get(course_id)

    def calculate_gpa(self, courses):
        scores = []
        credits = []
        for c in courses:
            if c.id in self.marks:
                scores.append(self.marks[c.id])
                credits.append(c.credit)

        if not credits:
            return None

        scores_arr = np.array(scores, dtype=float)
        credits_arr = np.array(credits, dtype=float)
        gpa = np.sum(scores_arr * credits_arr) / np.sum(credits_arr)
        return round(float(gpa), 2)

    def __repr__(self):
        return f"Student({self.id}, {self.name})"
