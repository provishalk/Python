import numpy as np

file = open("inputOne.csv")
movie_Data = np.loadtxt(file, delimiter=",")
print(movie_Data)
print(np.average(movie_Data))


a = np.array([1.5,"Vishal",3.7,4.8])
print(a)

b = np.array([[1,5,2,4],[8,5,2,4]])
print(b)

c = np.zeros(5)
print(c)

d = np.ones(6)
print(d)

f = np.random.rand(2,5)
print(f)

g= np.full((5,5),9)
print(g)

h= np.eye(3)
print(h)

a= np.array([[1,2,3],[4,5,6]])
print("array:\n",a)
print("shape:",a.shape)
print("rows:",a.shape[0])
print("colums:",a.shape[1])
