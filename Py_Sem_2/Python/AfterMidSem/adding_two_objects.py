class Num1:
    def __init__(self):
        self.a = 10

    def __add__(self, other):
        self.a = self.a + other.b

    def __mod__(self, other):
        print("modulus function of num1")\


    def __neg__(self):
        print("Operator Overloading for binary operator")


class Num2:
    def __init__(self):
        self.b= 30


x = Num1()
y = Num2()
x+y
x % y
+x
print(x.a)
