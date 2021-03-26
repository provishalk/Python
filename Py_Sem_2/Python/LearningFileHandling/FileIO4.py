f = open("input4.txt","wt")
f.writelines("Hai there\nHow are you?\nWelcome home!\n")
f.close()

f = open("input4.txt","rt")
for x in f:
    print(x)
f.close()
