arr = [2,6,7,8,11,15,17,21,26,27,31]
end = len(arr)-1
def binarySearch(arr,start,end,key):
    mid = int((start+end)/2)
    print("Start = {0} Mid = {1} End = {2}".format(start,mid,end))
    if arr[mid] == key:
        return mid
    elif start == end or mid == 0:
        return
    else:
        if key < arr[mid]:
            return binarySearch(arr,start,mid-1,key)
        else:
            return binarySearch(arr,mid+1,end,key)
x = binarySearch(arr,0,end,15)
print(x)