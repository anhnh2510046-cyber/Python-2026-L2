class Course:
    def __init__(self, cid, name, credit):
        self.id = cid
        self.name = name
        self.credit = credit

    def __repr__(self):
        return f"Course({self.id}, {self.name}, {self.credit} tin chi)"
