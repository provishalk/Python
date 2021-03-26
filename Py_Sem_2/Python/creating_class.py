# class method
# static method

class Employee:
    no_of_emps=0
    raise_amt = 1.04
    #class varibales
    def __init__(self,first, last ,pay):
        # instance varibale
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." +last +"@gmail.com"
        Employee.no_of_emps += 1
    def fullname(self):
        return f"{self.first} {self.last}"
    def emailID(self):
        return self.email

    @classmethod
    def is_working(cls):
        print("CLass Method")


emp1 = Employee("VISHAL","KUMAR",20000)
print(emp1.fullname())
emp1.is_working()

