import numpy as np
#calculation of the determinant
A = np.array([[0, 6, -2, -1, 5],
             [0, 0, 0, -9, -7],
             [0, 15, 35, 0, 0],
             [0, -1, -11, -2, 1],
             [-2, -2, 3, 0, -2]])
print("Matrix A :\n",A)
print("Determinant of Matrix A is:", np.linalg.det(A))

#Transpose of matrix
B = np.array([[0, 6, -2, -1, 5],
             [0, 0, 0, -9, -7],
             [0, 15, 35, 0, 0],
             [0, -1, -11, -2, 1],
             [-2, -2, 3, 0, -2]])
print("Matrix B:\n",B)
print("Transpose of Matix B:\n", np.transpose(B))

#Inverse of matrix
C = np.array([[-1, 1, 1, 1],
              [1, -1, 1, 1],
              [1, 1, -1, 1],
              [1, 1, 1, -1]])
print("Matrix C:\n",C)
print("Inverse of Matix C:\n", np.linalg.inv(C))

#Eigen value and EigenVector of 3X3 matix
D = np.array([[-2, -4, 2],
              [-2, 1, 2],
              [4, 2, -5]])
print("Matrix D:\n",D)
l1 ,l2= np.linalg.eig(B)
print( "Eigenvalues of the matrix:\n",l1)
print( "Eigenvectors of the matrix:\n",l2)

#Gauss Elemination Method
def gaussElimin(ob,obb):
    n=len(obb)
    for k in range(0,n-1):
        for i in range(k+1,n):
            if ob[i,k]!= 0.0:
                lem =ob[i,k]/obb[k,k]
                ob[i,k+1:n]=a[i,k+1:n] - lem*ob[k,k+1:n]
                obb[i]=b[i]-lem*b[k]
    for k in range(n-1,-1,-1):
        obb[k]=(obb[k]-np.dot(ob[k,k+1:n],obb[k+1:n]))/ob[k,k]
    return obb
o = np.matrix([[4,-2,1],[-2,4,-2],[1,-2,4]])
b = np.matrix([11,-16,17])
print("Matrix A:",o)
print("Matrix A:",b)
print("values:")
print("[[ x1 x2 x3]]")
print(gaussElimin(o,b))
