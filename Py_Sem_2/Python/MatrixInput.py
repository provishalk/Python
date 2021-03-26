import numpy as np

a = np.array([1,2,3,4])
print(a)

a = np.array([1.5,'harsha',3.7,4.8])
print(a)

b = np.array([[1,2,3,4],[5,6,7,8]])
print(b)

c = np.zeros(5)
print(c)

d = np.zeros((2,3))
print(d)

e = np.ones(5,dtype=np.int32)
print(e)

f = np.random.rand(2,3)
print(f)

g = np.full((2,2),7)
print(g)

# identity matrix
h = np.eye(3)
print(h)
print(h.ndim)

a = np.array([[1,2,3],[4,5,6]])
print('Array :','\n',a)
print('Shape :','\n',a.shape)
print('Rows = ',a.shape[0])
print('Columns = ',a.shape[1])

# size of array
a = np.array([[5,10,15],[20,25,20]])
print('Size of array :',a.size)
print('Manual determination of size of array :',a.shape[0]*a.shape[1])

# reshape
a = np.array([3,6,9,12])
a = np.reshape(a,(2,2))
print(a)


a = np.ones((2,2))
b = a.flatten()
c = a.ravel()
print('Original shape :', a.shape)
print('Array :','\n', a)
print('Shape after flatten :',b.shape)
print('Array :','\n', b)
print('Shape after ravel :',c.shape)
print('Array :','\n', c)

# transpose
a = np.array([[1,2,3],[4,5,6]])
b = np.transpose(a)
print('Original','\n','Shape',a.shape,'\n',a)
print('Expand along columns:','\n','Shape',b.shape,'\n',b)
print(a)
print(b)

#slicing
print("slicing")
a = np.array([1,2,3,4,5,6])
print(a[1:5:2])
print(a[1:6:2])

a = np.array([[1,2,3],
[4,5,6]])
print(a[0,0])
print(a[1,2])
print(a[1,0])

a = np.array([[1,2,3],[4,5,6]])
# print first row values
print('First row values :','\n',a[0:1,:])
# with step-size for columns
print('Alternate values from first row:','\n',a[0:1,::2])
#
print('Second column values :','\n',a[:,1::2])
print('Arbitrary values :','\n',a[0:1,1:3])

# concatenating arrays
a = np.arange(0,5).reshape(1,5)
b = np.arange(5,10).reshape(1,5)
print('Array 1 :','\n',a)
print('Array 2 :','\n',b)
print('Concatenate along rows :','\n',np.concatenate((a,b),axis=0))
print('Concatenate along columns :','\n',np.concatenate((a,b),axis=1))

