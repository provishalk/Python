f = open("input3.txt","wt")
f.writelines("This is the over written line")
f.close()

f = open("input3.txt","rt")
for x in f:
    print(x)
f.close()
