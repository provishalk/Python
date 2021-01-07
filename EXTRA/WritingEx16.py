from sys import argv
source , fileName = argv
print("Hello, today we are going to erase your file")
print("If you don't want to do that press control-c(c^)")
print("If you want to do that press enter")
input("?")

print("Opening the file")
txt = open(fileName,'w')

print("cotent erased")
#txt.truncate()

print("Enter three line for textfile")
line1 = input("Line1:")
line2 = input("Line2:")
line3 = input("Line3:")

print("Now, I am going to write these line into your file")

txt.write(line1)
txt.write("\n")
txt.write(line2)
txt.write("\n")
txt.write(line3)
txt.write("\n")

print("Going to close your file......\nCLOSED")
txt.close()