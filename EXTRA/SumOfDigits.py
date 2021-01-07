digit = 25315
hold = digit
sum = 0
while digit != 0:
    a = digit%10
    digit = int(digit/10)
    sum = sum + a
print(f"The Sum of Digits : {hold} are {sum} ")