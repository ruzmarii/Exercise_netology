class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):

        if not isinstance(grade, int) or grade < 1 or grade > 10:
            print("Ошибка: оценка должна быть целым числом от 1 до 10")
            return

        if course not in self.courses:
            print(f"Ошибка: студент {self.name} {self.surname} не записан на курс {course}")
            return

        if course not in lecturer.courses_attached:
            print(f"Ошибка: лектор {lecturer.name} {lecturer.surname} не ведет курс {course}")
            return

        if course in lecturer.grades:
            lecturer.grades[course].append(grade)
        else:
            lecturer.grades[course] = [grade]


class Lecturer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Reviewer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        """
        Метод для выставления оценки студенту за домашнее задание
        :param student: объект Student
        :param