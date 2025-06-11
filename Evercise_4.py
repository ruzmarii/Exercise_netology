class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer)
                and course in self.courses_in_progress
                and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        avg_grade = self._calculate_avg_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")

    def _calculate_avg_grade(self):
        if not self.grades:
            return 0
        total = sum(sum(grades) for grades in self.grades.values())
        count = sum(len(grades) for grades in self.grades.values())
        return round(total / count, 1)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Сравнение возможно только между студентами")
            return False
        return self._calculate_avg_grade() < other._calculate_avg_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        avg_grade = self._calculate_avg_grade()
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade}")

    def _calculate_avg_grade(self):
        if not self.grades:
            return 0
        total = sum(sum(grades) for grades in self.grades.values())
        count = sum(len(grades) for grades in self.grades.values())
        return round(total / count, 1)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Сравнение возможно только между лекторами")
            return False
        return self._calculate_avg_grade() < other._calculate_avg_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student)
                and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


def calculate_avg_hw_grade(students, course):
    total = 0
    count = 0
    for student in students:
        if course in student.grades:
            total += sum(student.grades[course])
            count += len(student.grades[course])
    if count == 0:
        return 0
    return round(total / count, 1)


def calculate_avg_lecture_grade(lecturers, course):
    total = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    if count == 0:
        return 0
    return round(total / count, 1)


def main():
    student1 = Student('Иван', 'Иванов', 'мужской')
    student1.courses_in_progress = ['Python', 'Git']
    student1.finished_courses = ['Введение в программирование']

    student2 = Student('Мария', 'Петрова', 'женский')
    student2.courses_in_progress = ['Python', 'Git']
    student2.finished_courses = ['Введение в программирование']

    lecturer1 = Lecturer('Алексей', 'Смирнов')
    lecturer1.courses_attached = ['Python', 'Git']

    lecturer2 = Lecturer('Елена', 'Кузнецова')
    lecturer2.courses_attached = ['Python', 'Git']

    reviewer1 = Reviewer('Дмитрий', 'Васильев')
    reviewer1.courses_attached = ['Python', 'Git']

    reviewer2 = Reviewer('Ольга', 'Соколова')
    reviewer2.courses_attached = ['Python', 'Git']

    reviewer1.rate_hw(student1, 'Python', 9)
    reviewer1.rate_hw(student1, 'Python', 8)
    reviewer1.rate_hw(student1, 'Git', 10)
    reviewer1.rate_hw(student1, 'Git', 9)

    reviewer2.rate_hw(student2, 'Python', 7)
    reviewer2.rate_hw(student2, 'Python', 9)
    reviewer2.rate_hw(student2, 'Git', 8)
    reviewer2.rate_hw(student2, 'Git', 10)

    student1.rate_lecture(lecturer1, 'Python', 10)
    student1.rate_lecture(lecturer1, 'Git', 9)
    student2.rate_lecture(lecturer1, 'Python', 8)
    student2.rate_lecture(lecturer1, 'Git', 9)

    student1.rate_lecture(lecturer2, 'Python', 7)
    student1.rate_lecture(lecturer2, 'Git', 8)
    student2.rate_lecture(lecturer2, 'Python', 9)
    student2.rate_lecture(lecturer2, 'Git', 10)

    print("Информация о студентах:")
    print(student1)
    print()
    print(student2)
    print("\nИнформация о лекторах:")
    print(lecturer1)
    print()
    print(lecturer2)
    print("\nИнформация о проверяющих:")
    print(reviewer1)
    print()
    print(reviewer2)

    print("\nСравнение студентов:")
    print(f"Средняя оценка {student1.name} {student1.surname} > "
          f"{student2.name} {student2.surname}: {student1 > student2}")

    print("\nСравнение лекторов:")
    print(f"Средняя оценка {lecturer1.name} {lecturer1.surname} > "
          f"{lecturer2.name} {lecturer2.surname}: {lecturer1 > lecturer2}")

    students_list = [student1, student2]
    lecturers_list = [lecturer1, lecturer2]
    course_name = 'Python'

    avg_hw_grade = calculate_avg_hw_grade(students_list, course_name)
    print(f"\nСредняя оценка за домашние задания по курсу {course_name}: "
          f"{avg_hw_grade}")

    avg_lecture_grade = calculate_avg_lecture_grade(lecturers_list, course_name)
    print(f"Средняя оценка за лекции по курсу {course_name}: "
          f"{avg_lecture_grade}")


if __name__ == '__main__':
    main()