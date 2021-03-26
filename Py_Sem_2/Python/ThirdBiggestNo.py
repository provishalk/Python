given_matrix = [[4, 5, 8], [7, 1, 45], [42, 27, 13]]
largest = given_matrix[0][0]
second_largest = largest
third_largest = largest
for i in given_matrix:
    for j in i:
        if(j > largest):
            largest = j
        elif(j >= second_largest and j< largest):
            second_largest = j
        elif (j >= third_largest and j < second_largest):
            third_largest = j
print(f"Third largest no in Matrix is: {third_largest}")