from abc import ABC,abstractmethod


class Employeee(ABC):
    @abstractmethod
    def empID(self):
        pass

    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"The Employee ID {self.id}"


class Manager(Employeee):
    def empID(self):
        return f"Employee ID method {self.id}"


# o = Employeee(21, "Vishal Kumar", 200000)

m = Manager(21, "Vishal Kumar", 200000)
print(m.empID())




