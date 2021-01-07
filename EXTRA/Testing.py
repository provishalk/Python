arr = [1,2,3,4,5,6,7,8,9]
i = 0
#RightShift
print(arr)

#for i in range(2):
#   i = len(arr)-1
#    temp=arr[i]
#    while i != 0:
#        arr[i] = arr[i-1]
#        i = i-1
#    arr[0]= temp
#print(arr)

#for j in range(2):
#    temp = arr[0]
#    for i in range(0,len(arr)-1):
#       arr[i] = arr[i+1]
#   arr[len(arr)-1] = temp
#print(arr)
arr1 = []
d=2
for value in (arr[d:] + arr[0:2]):
    arr1.append(value)
    print(value,end=" ")
print()
print(arr1)