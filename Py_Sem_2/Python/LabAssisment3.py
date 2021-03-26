mytuple = (2,5,8,1,78)
# myTupule.append(30);  'tuple' object has no attribute 'append'
# mytuple.extend(9) 'tuple' object has no attribute 'extend'
# mytuple.pop() 'tuple' object has no attribute 'pop'
# mytuple.push(10) 'tuple' object has no attribute 'push'
print(mytuple)
if 5 in mytuple:
    print("5 is present in mytuple")
else:
    print("mytuple dosent have 5")

# Print third element of tuple
print(f"Third element of is {mytuple[2]}")

print(hash("Vishal"))