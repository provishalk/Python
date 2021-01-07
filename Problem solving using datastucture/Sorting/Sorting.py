class Sorting:
    def bubbleSort(self,arr):
        for j in range(0,len(arr)-1,1):
            token = 0
            for i in range(0,len(arr)-1-j,1):
                if arr[i] > arr [i+1]:
                    temp = arr[i+1]
                    arr[i+1] = arr[i]
                    arr[i]=temp
                    token = 1;
            if token == 0:
                return arr
        return arr
    def selectionSort(self,arr):
        at = 0
        for j in range(0,len(arr),1):
            min = j
            for i in range(j,len(arr),1):
                if arr[i] < arr[min]:
                    min = i
                temp = arr[j]
                arr[j] = arr[min]
                arr[min] = temp
        return arr
    def insertionSort(self,arr):
        for i in range(1,len(arr),1):
            temp = arr[i]
            flag = 0;
            for j in range(i,0,-1):
                if temp < arr[j-1]:
                    t = arr[j]
                    arr[j] = arr[j-1]
                    arr[j-1] = t
                    flag = 1;
                if flag == 0:
                    break
        return arr

list = [9,8,7,6,65,4,3,2,1]
obj = Sorting()
print(obj.insertionSort(list))


