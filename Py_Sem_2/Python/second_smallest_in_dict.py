dic = {4: "harsha",
       1: "abi",
       5: "karikalan",
       9: "siddharth",
       2: "adhi",
       7: "nandini",
       8: "vanathi"}
smallest = 200000
second_smallest = smallest
for i in dic:
    if i <smallest:
        smallest = i
    elif i < second_smallest and i >smallest:
        second_smallest = i
for i in dic:
    if i > second_smallest:
        print(f"KEY : {i} VALUE : {dic[i]} ")
