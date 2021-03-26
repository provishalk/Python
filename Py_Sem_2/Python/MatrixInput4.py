import numpy as np
# Basic arithmetic operations on NumPy arrays
a = np.array([1,2,3,4,5])
print('Subtract :',a-5)
print('Multiply :',a*5)
print('Divide :',a/5)
print('Power :',a**2)
print('Remainder :',a%5)

# Mean, Median and Standard deviation
a = np.arange(5,15,2)
print(a)
print('Mean :',np.mean(a))
print('Standard deviation :',np.std(a))
print('Median :',np.median(a))

# Min-Max
a = np.array([[1,6],[4,3]])
# minimum along a column
print('Min :',np.min(a,axis=0))
# maximum along a row
print('Max :',np.max(a,axis=1))

# sorting
a = np.array([1,4,2,5,3,6,8,7,9])
print(a)
a = np.sort(a, kind='quicksort')
print(a)

a = np.array([[5,6,7,4],
              [9,2,3,7]])
# sort along the column
print('Sort along column :','\n',np.sort(a, kind='mergresort',axis=1))
# sort along the row
print('Sort along row :','\n',np.sort(a, kind='mergresort',axis=0))








