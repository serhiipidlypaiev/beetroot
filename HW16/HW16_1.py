class Person():
    def __init__(self, name, surname, birthdate, city) -> None:
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.city = city
        
    def change_name_surname(self, name, surname):
        self.name = name
        self.surname = surname
    
    def change_city(self, city):
        self.city = city
    
class Student(Person):
    def __init__(self, *args, group, scholarship) -> None:
        super().__init__(*args)
        self.gloup = group
        self.scholarship = scholarship
    
    def change_group(self, group):
        self.group = group
        
    def size_of_scholarship(self, scholarship):
        self.scholarship = scholarship
        
class Teacher(Person):
    def __init__(self, science, salary, class_teacher:bool, *args) -> None:
        super().__init__(*args)
        self.science = science
        self.salary = salary
        self.class_teacher = class_teacher
    
    def change_salary(self, salary):
        self.salary = salary
    
    def add_rem_class_teacher(self, class_teacher:bool):
        self.class_teacher = class_teacher
        