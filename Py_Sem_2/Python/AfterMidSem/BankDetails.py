class Bank:
    def __init__(self, accountno, name, balance):
        self.accountno = accountno
        self.balance = balance
        self.name = name

    def __str__(self):
        return f"The Saving account no is {self.accountno}, " \
               f"The account holder name is {self.name}, " \
               f"and the balance is :{self.balance}"

    def getBalance(self):
            return f"Balance is {self.balance}"

    def __add__(self, other):
        self.balance = self.balance + other


ronit = Bank(110, "Ronit", 64000)
print(ronit)
ronit + 34000
print(ronit)