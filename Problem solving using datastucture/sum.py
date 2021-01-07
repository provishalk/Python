def pairs(arr, n, sum):
    temp = False
    for i in range(0, n):
        for j in range(i + 1, n):
            if (arr[i] + arr[j] == sum):
                print("(", arr[i],",", arr[j],")")
                temp = True
    if temp== False:
        print("No pair can be Formed of Sum {}".format(n))

arr = [6,2,1,3,4,5]
n = len(arr)
sum = 5
pairs(arr, n, sum)