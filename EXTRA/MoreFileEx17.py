from sys import argv
from os.path import exists

Script , fromFile , toFile = argv

print(f"We are going to copy {fromFile} file content to {toFile}")
fileContent = open(fromFile)
destination = open(toFile,'w')
print(f"length of file is{len(fileContent.read())}")
print(f"Does the export file exist?{exists(toFile)}")
print("Press Enter to proceed and Press Contol-C to Abord")
input("?")
destination.write(fileContent.read())
print("Content is successfully copied")
fileContent.close()
destination.close()

