# Python program to explain os.mkdir() method 

# importing os module 
import os

# Directory
directory = "Task1"

# Parent Directory path
parent_dir = "E:/CodingZone/Python/FileHandling"

# Path
path = os.path.join(parent_dir, directory)
print(path)

# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
try:
    os.mkdir(path)
    print("Directory '% s' created" % directory)
except OSError as error:
    print(error)


