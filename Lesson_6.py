
from unicodedata import name


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_rate(self):
        sum1 = 0
        len1 = 0
        for course in self.grades:
            sum1 += sum(self.grades[course])
            len1 += len(self.grades[course])      
        if len1 != 0:
            res = round(sum1/len1, 2) 
            return res
        else:
            return 0

    def __str__(self):
        return f'''
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.avg_rate()}'''

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        elif self.avg_rate() > other.avg_rate():
            print(f'Средний балл {self.avg_rate()} выше у лектора {self.name}, чем {other.avg_rate()} у {other.name}')
        else:
            print(f'Средний балл {other.avg_rate()} выше у лектора {other.name}, чем {self.avg_rate()} у {self.name}')

        
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and (1 <= grade <= 10):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка')

    def __str__(self):
        return f'''Имя: {self.name}
Фамилия: {self.surname}'''
    

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
        self.courses_in_progress.remove(course_name)


    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and (course in self.courses_in_progress or course in self.finished_courses) and course in lecturer.courses_attached and (1 <= grade <= 10):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print('Ошибка')

    def avg_rate(self):
        return Lecturer.avg_rate(self)

    def __str__(self) -> str:
        return f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.avg_rate()}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
Завершенные курсы: {', '.join(self.finished_courses)}'''

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        elif self.avg_rate() > other.avg_rate():
            print(f'Средний балл {self.avg_rate()} выше у студента {self.name}, чем {other.avg_rate()} у {other.name}')
        else:
            print(f'Средний балл {other.avg_rate()} выше у студента {other.name}, чем {self.avg_rate()} у {self.name}')

# Создаем экземпляры и вызываем методы

first_lecturer = Lecturer('Ivan', 'Fedofovich')
first_lecturer.courses_attached += ['Git']
first_lecturer.courses_attached += ['Python']

second_lecturer = Lecturer('Semen', 'Petrovich')
second_lecturer.courses_attached += ['Python']
second_lecturer.courses_attached += ['Git']
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']

cool_student = Student('Kira', 'Light', 'male')
cool_student.courses_in_progress += ['Python']
cool_student.courses_in_progress += ['Git']
 
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

second_reviewer = Reviewer('Good', 'Teacher')
second_reviewer.courses_attached += ['Git']
 
cool_mentor.rate_hw(best_student, 'Python', 6)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 8)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(cool_student, 'Python', 7)
second_reviewer.rate_hw(best_student, 'Git', 10)
second_reviewer.rate_hw(cool_student, 'Git', 8)
second_reviewer.rate_hw(cool_student, 'Git', 10)

best_student.rate_lect(first_lecturer, 'Python', 1)
best_student.rate_lect(first_lecturer, 'Git', 4)
best_student.rate_lect(first_lecturer, 'Git', 10)
best_student.rate_lect(second_lecturer, 'Python', 10)
cool_student.rate_lect(second_lecturer, 'Git', 10)

best_student.add_courses('Python')

print(first_lecturer)
print(second_lecturer)

print(best_student)
print(cool_student)

print(cool_mentor)
print(second_reviewer)

first_lecturer < second_lecturer
best_student > cool_student

# Реализуем функцию подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса

students_list = [best_student, cool_student]

def avr_course_hw(list, course):
    sum1 = 0
    len1 = 0
    for student in list:
        for i in student.grades:
            if i == course:
                sum1 += sum(student.grades[i])
                len1 += len(student.grades[i])        
    res = round(sum1/len1, 2) 
    print(f'Средняя оценка за домашние задания по курсу {course} составляет {res} по всем студентам')
    return res

avr_course_hw(students_list, 'Git')   
    
# Реализуем функцию подсчета средней оценки за лекции всех лекторов в рамках курса 

lect_list = [first_lecturer, second_lecturer]

def avr_course_lect(list, course):
    sum1 = 0
    len1 = 0
    for lecturer in list:
        for i in lecturer.grades:
            if i == course:
                sum1 += sum(lecturer.grades[i])
                len1 += len(lecturer.grades[i])        
    res = round(sum1/len1, 2) 
    print(f'Средняя оценка за лекции по курсу {course} составляет {res}')
    return res

avr_course_lect(lect_list, 'Git')

