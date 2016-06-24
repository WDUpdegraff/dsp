# Matrix Algebra

import numpy as np

A = np.array([[1,2,3],[2,7,4]])
B = np.array([[1,-1],[0,1]])
C = np.array([[5,-1],[9,1],[6,0]])
D = np.array([[3,-2,-1],[1,2,3]])
u = np.array([[6,2,-3,5]])
v = np.array([[3,5,-1,4]])
w = np.array([[1],[8],[0],[5]])
alpha = 6

def printshape(mat,name,probnum):
    print(probnum+': '+name+' is '+str(mat.shape[0])+' by '+str(mat.shape[1]))

def addifcan(mat1,mat2):
    if mat1.shape == mat2.shape:
        return ' = '+str(mat1+mat2)
    else:
        return ' is not defined.'

def multifcan(mat1,mat2):
    if mat1.shape[1]==mat2.shape[0]:
        return ' = '+str(np.dot(mat1,mat2))
    else:
        return ' is not defined.'

#These print out answers, problem by problem.
printshape(A,'A','1.1')
printshape(B,'B','1.2')
printshape(C,'A','1.3')
printshape(D,'D','1.4')
printshape(u,'u','1.5')
printshape(w,'w','1.6')
print('\n2.1: u+v = '+str(u+v))
print('2.2: u-v = '+str(u-v))
print('2.3: alpha*u = '+str(alpha*u))
print('2.4: u*v = '+str(u*v))
print('2.5: ||u|| = '+str(np.linalg.norm(u))+'\n')
print('3.1: A+C'+addifcan(A,C))
print('3.2: A-C^T'+addifcan(A,-1*C.transpose()))
print('3.3: C^T+3D'+addifcan(C.transpose(),3*D))
print('3.4: BA'+multifcan(B,A))
print('3.5: B(A^T)'+multifcan(B,A.transpose()))
print('3.6: BC'+multifcan(B,C))
print('3.7: CB'+multifcan(C,B))
print('3.8: B^4 = '+str(np.dot(np.dot(B,B),np.dot(B,B))))
print('3.9: A(A^T)'+multifcan(A,A.transpose()))
print('3.10:(D^T)D'+multifcan(D.transpose(),D))

#RESULTS FOLLOW (printed directly)

#1.1: A is 2 by 3
#1.2: B is 2 by 2
#1.3: A is 3 by 2
#1.4: D is 2 by 3
#1.5: u is 1 by 4
#1.6: w is 4 by 1
#
#2.1: u+v = [[ 9  7 -4  9]]
#2.2: u-v = [[ 3 -3 -2  1]]
#2.3: alpha*u = [[ 36  12 -18  30]]
#2.4: u*v = [[18 10  3 20]]
#2.5: ||u|| = 8.60232526704
#
#3.1: A+C is not defined.
#3.2: A-C^T = [[-4 -7 -3]
# [ 3  6  4]]
#3.3: C^T+3D = [[14  3  3]
# [ 2  7  9]]
#3.4: BA = [[-1 -5 -1]
# [ 2  7  4]]
#3.5: B(A^T) is not defined.
#3.6: BC is not defined.
#3.7: CB = [[ 5 -6]
# [ 9 -8]
# [ 6 -6]]
#3.8: B^4 = [[ 1 -4]
# [ 0  1]]
#3.9: A(A^T) = [[14 28]
# [28 69]]
#3.10:(D^T)D = [[10 -4  0]
# [-4  8  8]
# [ 0  8 10]]
