import abc

class Rectangle:
   def __init__(self, x,y):
      self.l = x
      self.b=y
   def area(self):
      return "Rectangle Class"


class Square:
   def __init__(self, x,y):
      self.l = x
      self.b=y
   def area(self):
      return "Sqaure Class"


class Childc(Rectangle,Square):
    pass


r = Square(10,20)
print('area: ', r.area())