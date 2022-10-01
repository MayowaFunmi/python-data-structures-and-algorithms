# enter teacher details

class Teacher(object):
    def __init__(self):
        self.id = 0
        self.first_name = ""
        self.last_name = ""
        self.all_teachers = []
        self.teachers_list = []
        print(self.id, self.first_name, self.last_name)
        
    def __str__(self):
        return f"#ID: {self.id}, Teacher: {self.first_name} {self.last_name}"
        
    def all(self):
        return self.all_teachers

class Subject(Teacher):
    def __init__(self):
        Teacher.__init__(self)
        self.id = 0
        self.name = ""
        self._class = ""
        self.periods_per_week = ''
        self.min_period = 0
        self.max_period = 0
        self.all_subjects = []
        self.all_teachers = []
        self.subject_list = []
        self.class_list = []
        self.senior1A = {}
        self.senior1B = {}
        self.senior1C = {}
        self.senior2A = {}
        self.senior2B = {}
        self.senior2C = {}
        self.senior3A = {}
        self.senior3B = {}
        self.senior3C = {}
        self.s1A_subjects = []
        self.s1B_subjects = []
        self.s1C_subjects = []
        self.s2A_subjects = []
        self.s2B_subjects = []
        self.s2C_subjects = []
        self.s3A_subjects = []
        self.s3B_subjects = []
        self.s3C_subjects = []
        self.teacher_subjects = []


    def __str__(self):
        return f"Subject Name = {self.name}, Class = {self._class}, Periods per week = {self.periods_per_week}"
    
    def add_teachers(self, id, f_name, l_name):
        self.id = id
        self.first_name = f_name.capitalize()
        self.last_name = l_name.capitalize()
        #for  i in self.all_teachers:
            #if i[0] == self.id:
                #error = "teacher with ID " + self.id + " already exists"
                #print(error)
            #else:
        self.all_teachers.append([self.id, self.first_name, self.last_name])
        return self.all_teachers
        
    def add_teachers_subject(self):
        for teacher in self.all_teachers:
            if not teacher[0] in self.teacher_subjects:
                self.teacher_subjects.append(teacher)
            for subject in self.all_subjects:
                for x in self.teacher_subjects:
                    if teacher[0] == subject[0] and teacher[0] == x[0] and not subject[1] in x:
                        x.append(subject[1])
                        x.append(subject[2])
                    if teacher[0] == subject[0] and teacher[0] == x[0] and subject[1] in x and subject[2] not in x:
                        x.append(subject[2])
                        
        return self.teacher_subjects
        
    def show_teacher_subjects(self):
        return self.teacher_subjects
    
    def show_teachers(self):
        return self.all_teachers
        
    def s1A_periods(self, subject):
        sum = 0
        for i in self.all_subjects:
            if i[2] == "SS1A":
                sum = sum + i[3]
        self.senior1A["SS1A"] = sum
        return self.senior1A

    def s1B_periods(self, subject):
        sum = 0
        for i in self.all_subjects:
            if i[2] == "SS1B":
                sum = sum + i[3]
        self.senior1B["SS1B"] = sum
        return self.senior1B
    
    def s1C_periods(self, subject):
        sum = 0
        for i in self.all_subjects:
            if i[2] == "SS1C":
                sum = sum + i[3]
        self.senior1C["SS1C"] = sum
        return self.senior1C
        
    def s2A_periods(self, subject):
        sum = 0
        for i in self.all_subjects:
            if i[2] == "SS2A":
                sum = sum + i[3]
        self.senior2A["SS2A"] = sum
        return self.senior2A

    def s2B_periods(self, subject):
        sum = 0
        for i in self.all_subjects:
            if i[2] == "SS2B":
                sum = sum + i[3]
        self.senior2B["SS2B"] = sum
        return self.senior2B
    
    def s2C_periods(self, subject):
        sum = 0
        for i in self.all_subjects:
            if i[2] == "SS2C":
                sum = sum + i[3]
        self.senior2C["SS2C"] = sum
        return self.senior2C
        

    def s3A_periods(self, subject):
        sum = 0
        for i in self.all_subjects:
            if i[2] == "SS3A":
                sum = sum + i[3]
        self.senior3A["SS3A"] = sum
        return self.senior3A

    def s3B_periods(self, subject):
        sum = 0
        for i in self.all_subjects:
            if i[2] == "SS3B":
                sum = sum + i[3]
        self.senior3B["SS3B"] = sum
        return self.senior3B
    
    def s3C_periods(self, subject):
        sum = 0
        for i in self.all_subjects:
            if i[2] == "SS3C":
                sum = sum + i[3]
        self.senior3C["SS3C"] = sum
        return self.senior3C
    
    # list each class sibjects
    def subject_1A(self, subject):
        if not subject in self.s1A_subjects:
            self.s1A_subjects.append(subject)
        return self.s1A_subjects
        
    def subject_2A(self, subject):
        if not subject in self.s2A_subjects:
            self.s2A_subjects.append(subject)
        return self.s2A_subjects
        
    def subject_3A(self, subject):
        if not subject in self.s3A_subjects:
            self.s3A_subjects.append(subject)
        return self.s3A_subjects
        
    def subject_1B(self, subject):
        if not subject in self.s1B_subjects:
            self.s1B_subjects.append(subject)
        return self.s1B_subjects
        
    def subject_2B(self, subject):
        if not subject in self.s2B_subjects:
            self.s2B_subjects.append(subject)
        return self.s2B_subjects
    
    def subject_3B(self, subject):
        if not subject in self.s3B_subjects:
            self.s3B_subjects.append(subject)
        return self.s3B_subjects
        
    def subject_2C(self, subject):
        if not subject in self.s2C_subjects:
            self.s2C_subjects.append(subject)
        return self.s2C_subjects
        
    def subject_3C(self, subject):
        if not subject in self.s3C_subjects:
            self.s3C_subjects.append(subject)
        return self.s3C_subjects
        
    def subject_1C(self, subject):
        if not subject in self.s1C_subjects:
            self.s1C_subjects.append(subject)
        return self.s1C_subjects
    
    def add_subject(self, name):
        if not name in self.subject_list:
            self.subject_list.append(name)
        return f"Total Subjects = {len(self.subject_list)} - List = {self.subject_list}"
    
    def add_class(self, _class):
        if not _class in self.class_list:
            self.class_list.append(_class)
        return self._class
    
    def save_subjects(self, id, name, _class, periods_per_week, min_period, max_period):
        self.id = id
        self.name = name.capitalize()
        self._class = _class
        self.periods_per_week = periods_per_week
        self.min_period = min_period
        self.max_period = max_period
        self.all_subjects.append([self.id, self.name, self._class, self.periods_per_week, self.min_period, self.max_period])
        #print(self.all_subjects)
        # add teacher
        #self.add_teacher()
        # add class
        self.add_class(self._class)
        # add subject to list
        self.add_subject(self.name)
        # add number of periods for each subject
        if _class == "SS1A":
            self.s1A_periods(self.name)
            self.subject_1A(self.name)
        elif _class == "SS1B":
            self.s1B_periods(self.name)
            self.subject_1B(self.name)
        elif _class == "SS1C":
            self.s1C_periods(self.name)
            self.subject_1C(self.name)
        elif _class == "SS2A":
            self.s2A_periods(self.name)
            self.subject_2A(self.name)
        elif _class == "SS2B":
            self.s2B_periods(self.name)
            self.subject_2B(self.name)
        elif _class == "SS2C":
            self.s2C_periods(self.name)
            self.subject_2C(self.name)
        elif _class == "SS3A":
            self.s3A_periods(self.name)
            self.subject_3A(self.name)
        elif _class == "SS3B":
            self.s3B_periods(self.name)
            self.subject_3B(self.name)
        elif _class == "SS3C":
            self.s3C_periods(self.name)
            self.subject_3C(self.name)
            
    def print_subjects(self):
        for i in range(len(self.all_subjects)):
            print(self.all_subjects[i])
            #return self.all_subjects[i]
        return
    
    def print_all(self):
        return self.all_subjects
        
    def all_ss1A_periods(self):
        return self.senior1A
    def all_ss1B_periods(self):
        return self.senior1B
    def all_ss1C_periods(self):
        return self.senior1C

    def all_ss2A_periods(self):
        return self.senior2A
    def all_ss2B_periods(self):
        return self.senior2B
    def all_ss2C_periods(self):
        return self.senior2C

    def all_ss3A_periods(self):
        return self.senior3A
    def all_ss3B_periods(self):
        return self.senior3B
    def all_ss3C_periods(self):
        return self.senior3C
        