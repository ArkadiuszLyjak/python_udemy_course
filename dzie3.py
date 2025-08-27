class Human:
    ALLOWED_GENDER = ["male", "female"]
    ALLOWED_RACES = ["White", "Black", "Asian", "Latino"]

    def __init__(self, kind, race, age):
        if kind not in Human.ALLOWED_GENDER:
            raise ValueError(f"Kind must be in {Human.ALLOWED_GENDER}")
        if race not in Human.ALLOWED_RACES:
            raise ValueError(f"Race must be in {Human.ALLOWED_RACES}")
        self.kind = kind
        self.race = race
        self.age = age
        if age < 0 and not isinstance(age, int):
            raise ValueError("Age must be a positive integer")

        print("Human konstruktor")

    def print_human_info(self):
        print(f"Kind: {self.kind}")
        print(f"Race: {self.race}")
        print(f"Age: {self.age}")
        print("to byla metoda \"print_human_info\"\n\n")


class Student(Human):
    def __init__(self, name, school, kind, race, age):
        super().__init__(kind, race, age)
        self.name = name
        self.school = school
        print("Student konstruktor")

    def print_student_info(self):
        super().print_human_info()
        print(f"Name: {self.name}")
        print(f"School: {self.school}")
        print("to byla metoda \"print_student_info\"\n\n")


class Teacher(Student):
    def __init__(self, name, school, kind, race, age, rank):
        super().__init__(name, school, kind, race, age)
        self.rank = rank
        print("Teacher konstruktor")

    def print_teacher_info(self):
        super().print_student_info()
        print(f"Rank: {self.rank}")
        print("to byla metoda \"print_teacher_info\"\n\n")


teacher = Teacher("John", "High School", "male", "White", 35, "professor")
teacher.print_teacher_info()
