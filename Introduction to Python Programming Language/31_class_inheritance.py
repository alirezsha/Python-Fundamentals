class Person():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
    def print_name(self):
        print(self.name, self.surname)

class Student(Person):
    def __init__(self, name, surname, grade):
        super().__init__(name, surname)
        self.gradelevel = grade
        
    def print_student(self):
        print(self.name, self.surname, self.gradelevel)