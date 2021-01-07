from sys import argv

source , filename = argv
#This line Open the text file for future oprations
txt = open(filename)

print(f"here's your file {filename}")
#The file we opend in line 5 that file we are printing with the help of read
print(txt.read())

print("Type the filename again:")
#In this line we take input from user that which file the user want to open
fileAgain =input("> ")

txtAgain = open(fileAgain)
print(txtAgain.read())