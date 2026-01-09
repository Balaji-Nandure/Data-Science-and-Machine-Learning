class BankAccount:
    def __init__(self, name, balance = 0):
        self.name = name #public
        # self._balance = balance #protected
        self.__balance = balance #private
    
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, balance):
        self.__balance = balance

acc1 = BankAccount("Balaji", 1000)
acc1.get_balance()
acc1.set_balance(2000)
acc1.get_balance()
 
acc2 = BankAccount("Dipti", 2000)


#=================Inheritance==============================

class Employee:
    def __init__(self, name):
        self.name = name
    start_time = 10
    end_time  = 6

class Teacher(Employee):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    
class Principal(Employee):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    
teacher = Teacher("Math")
print(teacher.subject)
print(teacher.start_time)
print(teacher.end_time)

