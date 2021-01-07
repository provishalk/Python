digit = 1769
orignal = str(digit)
temp=0
while digit != 0:
    temp = temp*10
    temp = temp + digit%10
    digit = int(digit/10)
print(temp)