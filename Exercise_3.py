class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Reviewer(Person):
    def __str__(self):
        return super().__str__()


class Lecturer(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecture_grades = {}

    def __str__(self):
        avg_grade = self._calculate_average_grade()
        return super().__str__() + f"\nСредняя оценка за лекции: {avg_grade:.1f}"

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_average_grade() < other._calculate_average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return abs(self._calculate_average_grade() - other._calculate_average_grade()) < 1e-9

    def _calculate_average_grade(self):
        if not self.lecture_grades:
            return 0
        total = sum(sum(grades) for grades in self.lecture_grades.values())
        count = sum(len(grades) for grades in self.lecture_grades.values())
        return total / count


class Student(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_in_progress = []
        self.finished_courses = []

    def __str__(self):
        avg_grade = self._calculate_average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return (super().__str__() +
                f"\nСредняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_average_grade() < other._calculate_average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return abs(self._calculate_average_grade() - other._calculate_average_grade()) < 1e-9

    def _calculate_average_grade(self):
        if not self.grades:
            return 0
        total = sum(sum(grades) for grades in self.grades.values())
        count = sum(len(grades) for grades in self.grades.values())
        return total / count


reviewer = Reviewer("Some", "Buddy")
print(reviewer)

lecturer = Lecturer("Some", "Buddy")
lecturer.lecture_grades = {"Python": [10, 9, 8]}
print(lecturer)

student = Student("Rudy", "Enan")
student.grades = {"Python": [10, 9, 8]}
student.courses_in_progress = ["Python", "Git"]
student.finished_courses = ["Введение в программирование"]
print(student)

lecturer1 = Lecturer("John", "Doe")
lecturer1.lecture_grades = {"Math": [9, 9, 9]}
lecturer2 = Lecturer("Jane", "Smith")
lecturer2.lecture_grades = {"Math": [8, 8, 8]}

print(lecturer1 > lecturer2)
print(lecturer1 == lecturer2)

student1 = Student("Alice", "Johnson")
student1.grades = {"Python": [10, 10, 10]}
student2 = Student("Bob", "Williams")
student2.grades = {"Python": [9, 9, 9]}

print(student1 > student2)
print(student1 == student2)