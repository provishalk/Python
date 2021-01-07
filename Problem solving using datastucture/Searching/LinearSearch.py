import random
arr = [3,2,1,5,2,3,6,5,4,8,9,7,5,6,4,2,1,5,2]
#Method For LinearSearch
def linearSearch(arr,key):
    for x in range(0, len(arr)):
        if key == arr[x]: return x  #It will return the index number where value present
    return False
print(linearSearch(arr,5))
