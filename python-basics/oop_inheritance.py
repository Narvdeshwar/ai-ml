class Employee:
    start_time="8:00 am"
    end_time="6:00 pm"

class Teacher(Employee):
    def __init__(self,subject,name):
        self.subject=subject
        self.name=name

    def get_teacher_info(self):
        print(f"The teacher name is {self.name} and he teaches {self.subject} and he arrived at {self.start_time} and left the college at {self.end_time}")

class Administartor(Employee):
    def __init__(self,department,name):
        self.department=department
        self.name=name

    def get_admin_info(self):
        print(f"The admin name is {self.name} and he work in department of {self.department} and he arrived at {self.start_time} and left the institute at {self.end_time}")

t1=Teacher("english","cUT PIT")
t1.get_teacher_info()

a1=Administartor("IT","Brad pit")
a1.get_admin_info()
