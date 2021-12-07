class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_stuents):
        self.name = name
        self.max_students = max_stuents
        # add students to the course object
        self.students = []
        self.is_active = False

    # method to add studwnt object into the list
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_avaerage_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)


student_1 = Student('Tim', 19, 78)
student_2 = Student('Bola', 22, 56)
student_3 = Student('Mayowa', 32, 99)

course = Course('Science', 4)
course.add_student(student_3)
course.add_student(student_1)
#print(student_1.get_grade())
print(course.students) # returns the objects of students
print(course.students[0].name)  # name of student
print(course.get_avaerage_grade())