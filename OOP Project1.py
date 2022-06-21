class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_f_s(self, lecturer, course, grade_f_s):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.rating:
                lecturer.rating[course] += [grade_f_s]
            else:
                lecturer.rating[course] = [grade_f_s]
        else:
            return 'Ошибка'

    average_grade = 0

    def __str__(self):
        all_grades = []
        for course in self.grades:
            all_grades.extend(self.grades[course])
        if len(all_grades) > 0:
            average_grade = round(sum(all_grades) / len(all_grades), 10)
        else:
            average_grade = 0
        return f'Студент:\nИмя:{self.name}\nФамилия:{self.surname}\nКурсы в процессе изучения:{self.courses_in_progress}\nЗавершенные курсы:{self.finished_courses}\nСредняя оценка за ДЗ:{average_grade}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Укажите студентов!'
        return self.average_grade > other.average_grade


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    rating = {}
    average_rating = 0

    def __str__(self):
        rate = []
        for course in self.courses_attached:
            rate.extend(self.rating[course])
        if len(rate) > 0:
            average_rating = round(sum(rate) / len(rate), 1)
        else:
            average_rating = 0
        return f'Лектор:\nИмя:{self.name}\nФамилия:{self.surname}\nСредний рейтинг за Л:{average_rating}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Укажите Лекторов!'
        return self.average_rating > other.average_rating


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Проверяющий:\nИмя:{self.name}\nФамилия:{self.surname}'


l1 = Lecturer('Julia', 'Ivanova')
l2 = Lecturer('Sergey', 'Petrov')
# print(l1.__lt__(l2))
st1 = Student('Petr', 'Pavlov', 'm')
st2 = Student('Maria', 'Daryina', 'w')
# print(st2)
r1 = Reviewer('Michail', 'Vasin')
r2 = Reviewer('Olga', 'Alexandrova')

st1.courses_in_progress += ['Python']
st2.courses_in_progress += ['Python']

l1.courses_attached += ['Python']
l2.courses_attached += ['Python']

r1.courses_attached += ['Python']
r2.courses_attached += ['Python']

r1.rate_hw(st1, 'Python', 9)
r2.rate_hw(st2, 'Python', 8)
r1.rate_hw(st2, 'Python', 9)
r2.rate_hw(st1, 'Python', 8)
r1.rate_hw(st1, 'Python', 10)
r2.rate_hw(st2, 'Python', 10)
# print(st1.grades)
# print(st2.grades)
st1.rate_f_s(l1, 'Python', 10)
st2.rate_f_s(l2, 'Python', 10)
# print(l1.rating)
# print(l2)


def av_st_g(all_st, course_name):
    all_st = [st1, st2]
    for s in all_st:
        all_gr = 0
        for course_name in Student.grades.values:
            sum(Student.grades.values) / len(Student.grades.values)