def quickSort(array,lb,ub):
    start = lb
    end = ub
    pivot = array[lb]
    while(start < end):
        while (array[start] <= pivot):
                start = start + 1
                if start == len(array):
                    break
        while (array[end] > pivot):
            end = end - 1
            if end == -1:
                break
        if start < end:
            array[start], array[end] = array[end], array[start]
    array[lb], array[end] = array[end], array[lb]
    return end
def sort(array,start,end):
    if start < end:
        loc = quickSort(array,start,end)
        sort(array,start,loc-1)
        sort(array,loc+1,end)
sort(list, 0, len(list)-1)
print(list)
