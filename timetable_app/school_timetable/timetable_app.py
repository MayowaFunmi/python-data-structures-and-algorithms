import random

class Subject:
    def __init__(self):
        #self.sub_name = sub_name
        self.all_subjects = []
        self.subjects_list = []
        self.each_teacher = {}
        
    def __str__(self):
        return f"All subject: {self.all_subjects}"
        
    #add subject
    def add_subject(self):
        subject_list = ["maths", "english", "physics", "chemistry", "biology", 
            "civic", "account", "commerce", "agric sc", "geography", "economics",
        "lit in english"]
        new_subject = True
        while new_subject:
            name = input("Enter Subject: ")
            min_period = int(input("Enter Subject Minimum Period: "))
            max_period = int(input("Enter Subject Maximum Period: "))
            subject_name = name.capitalize()
            if not subject_name in self.subjects_list:
                self.subjects_list.append(subject_name)
                self.all_subjects.append([subject_name, min_period, max_period])
            else:
                print("Sorry, you have already added that subject")
            
            question = input("Do you want to add another question? (type y for yes and n for no): ")
            if question.lower() == "n":
                new_subject = False
            elif question.lower() == "y":
                new_subject = True
            else:
                print("You have entered invalid response. pls try again")
                self.add_subject()
        return self.all_subjects
        
    def teacher_subjects(self):
            # 
            new_subject = True
            while new_subject:
                if self.id in self.each_teacher:
                    teacher_subjects = self.each_teacher[self.id]
                    print("The following are your subjects: ", teacher_subjects)
                    question = input("Do you want to add another subject? y or n: ")
                    if question.lower() == "n":
                        new_subject = False
                    elif question.lower() == "y":
                        subject_name = input("Enter Subject name: ")
                        subject_name = subject_name.capitalize()
                        if not subject_name in self.subjects_list:
                            print(subject_name, " is not in the available subject list but will be added now")
                            min_period = int(input("Enter Subject Minimum Period: "))
                            max_period = int(input("Enter Subject Maximum Period: "))
                            self.subjects_list.append(subject_name)
                            self.all_subjects.append([subject_name, min_period, max_period])
                        teacher_subjects.append(subject_name)
                        new_subject = True
                    else:
                        print("Invalid choice. Try again")
                        self.teacher_subjects()
                else:
                    print("You are adding your first subject")
                    subject_name = input("Enter Subject name: ")
                    subject_name = subject_name.capitalize()
                    if not subject_name in self.subjects_list:
                        print(subject_name, " is not in the available subject list but will be added now")
                        min_period = int(input("Enter Subject Minimum Period: "))
                        max_period = int(input("Enter Subject Maximum Period  "))
                        self.subjects_list.append(subject_name)
                        self.all_subjects.append([subject_name, min_period, max_period])
                    self.each_teacher[self.id] = [subject_name]
            return self.each_teacher
            
        #add duration
        #add max and min period
        
class Teacher(Subject):
    def __init__(self, id, first_name, last_name):
        super().__init__()
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        
    def __str__(self):
        return f"Teacher Details: #ID: {self.id} - {self.first_name} {self.last_name}"


# add subject
#sub1 = Subject()
#print(sub1.add_subject())
t1 = Teacher(1, "Mayowa", "Akinade")
print(t1.teacher_subjects())

