# class Car:
#     # class variable , constant;
#     carType = "HatchBack"
#
#     def __init__(self,name,make):
#         self.name = name
#         self.make = make
#
#     def toString(self):
#         return f"This is a {self.name} carType is "
#
#
#
#
# c = Car("Polo", "Volkswagen")
# # print(Car("OOOO","AUDI").make)
# print(c.toString())
# print(Car.car_type)

class SUV:
    carType = "SUV"

    def __init__(self,name,make):
        self.name = name
        self.make = make

    def to_string(self):
        return f"Name of car : {self.name} manufactured by {self.make} is a type of {SUV.carType}"

    @classmethod
    def car_type(cls):
        return f"car Type is {cls.carType}"

    @staticmethod
    def get_fuel_type(self):
        return f"Fuel type is diesel {self.car_type()}"


obj = SUV("Scorpio", "Mahindra")
print(obj.to_string())
print(SUV.car_type())
print(SUV.get_fuel_type(obj))
