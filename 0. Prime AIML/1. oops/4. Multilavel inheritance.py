class Teacher:
    def __init__(self, salary):
        self.salary = salary

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class TA(Teacher, Student):
    def __init__(self, salary, name, age):
        # This is how we do multiple inheritance in python
        Teacher.__init__(self, salary)
        Student.__init__(self, name, age)
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")