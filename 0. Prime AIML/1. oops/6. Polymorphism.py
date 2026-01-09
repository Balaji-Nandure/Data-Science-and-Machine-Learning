# polymorphism is the ability to take many forms
# e.g plus(+) operator can be used to add two numbers, or two strings

# 1. function overloading (same function name with different parameters)
# 2. duck typing (if it walks like a duck, quacks like a duck, then it is a duck)


class Employee:
    def get_designation(self):
        return "Employee"

# note: these classes are inheriting the Employee class
# but they have different implementation of the get_designation method
class Manager(Employee):
    def get_designation(self):
        return "Manager"

class Developer(Employee):
    def get_designation(self):
        return "Developer"

# ==================Duck typing example==================
class Cat:
    def make_sound(self):
        print("Meow Meow")

class Dog:
    def make_sound(self):
        print("Woof Woof")

# here both the classes have the make_sound method
# but the implementation is different
# this is called duck typing
# if it walks like a duck, quacks like a duck, then it is a duck

