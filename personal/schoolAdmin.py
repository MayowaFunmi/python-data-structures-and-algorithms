class School:
    def __init__(self, sch_name: str, sch_type: str, location: str,):
        self.sch_name = sch_name
        self.sch_type = sch_type
        self.location = location

    def __str__(self):
        return f'Welcome to {self.sch_name}, located in {self.location}'

    def get_sch_name(self):
        return self.sch_name

    def get_sch_location(self):
        return self.location


class Student(School):
    def __init__(self, sch_name, sch_type, location, name: str, age: int, gender: str):
        super().__init__(sch_name, sch_type, location)
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f'I am {self.name} and my school is {self.sch_name} at {self.location}'

    def student_details(self):
        return f'I am {self.name}, a {self.gender} of {self.age} years who attends {self.sch_name} in {self.location}'


sch1 = School('Victop College', 'Secindary School', 'Ibadan')
print(sch1)

std1 = Student('Army Barracks', 'Govt Sec Sch', 'Iwo Road Ibadan', 'Mayowa', 33, 'Male')
print(std1)
print(std1.student_details())