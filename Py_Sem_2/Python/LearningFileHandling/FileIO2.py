f = open("input2.txt","at")
f.writelines("This is a new file")
f.close()

f = open("input2.txt","rt")
for x in f:
    print(x)
f.close()

