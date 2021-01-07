import os
path = "E:\CodingZone\Python\FileHandling\Task1"
f = []

for (dirpath, dirname, filename) in os.walk(path):
    f.extend(filename)
    break
for i in f:
    try:
        os.mkdir(os.path.join(path, i[0]))
    except OSError as error:
        pass
    source = os.path.join(path, i)
    destination = os.path.join(os.path.join(path, i[0]), i)
    os.rename(source, destination)
print("Transfer Completed....")
# Dynamic path
# Current python file ignore
