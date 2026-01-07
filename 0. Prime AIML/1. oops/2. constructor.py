class Student:
    # class variable is a variable that is shared by all objects of the class
    school_name = "ABC School"

    # constructor is a special method that is called when an object is created
    # constructor is used to initialize the object
    # constructor is called automatically when an object is created
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # we are passing self argument to the method
    # this is instance method which is used to access the instance variables
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

    # class method is a method that is shared by all objects of the class
    # class method is used to access the class variables
    @classmethod # decorator is used to convert a method into a class method
    def display_school_name(cls):
        print(f"School Name: {cls.school_name}")

    # static method is a method that is not related to the class or instance
    @staticmethod # decorator is used to convert a method into a static method
    def display_static_method():
        print("This is a static method")


student1 = Student("John", 20)
student1.display()

student2 = Student("Jane", 21)
student2.display()
