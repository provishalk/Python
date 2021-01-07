import os
path = "E:/CodingZone/Python/"
f = []
for (dirpath, dirnames, filenames) in os.walk(path):
    f.extend(filenames)
    break
for i in f:
    print(i)
