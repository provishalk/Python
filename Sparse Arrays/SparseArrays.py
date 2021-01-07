arr= ["abc","bca","mca","mca","bca"]
print(arr)
query = ["mca","bca"]
temp = []
for j in query:
    t=0
    for i in arr:
        if i == j:
            t += 1
    temp.append(t)
print(temp)