#frozenSet
employeeDict = {"name": "Vishal Kumar", "age": 22, "salary": 20000}
employeeattributeSet = frozenset(employeeDict)
# print(employeeattributeSet[1])


def mutualExclution():
    print("now one thread can run")

def runMultipleThreads():
    print("now more than one thread can run")
criticalSection = False
if(criticalSection):
    mutualExclution()
else:
    runMultipleThreads()

# memory view
# Modifying internal data using memory view
# random bytearray
byte_array = bytearray('XYZ', 'utf-8')
print('Before update:', byte_array)

mem_view = memoryview(byte_array)

# update 2nd index of mem_view to J
mem_view[2]= 74
print('After update:', byte_array)