#!/usr/bin/python3

import numpy as np

aList = [1, 2, 3, 4, 5]
npArray = np.array(aList)
print(aList)
print(npArray)
print(type(aList))
print(type(npArray))

print(aList + aList)
print(npArray + npArray)
print(aList * 3)
print(npArray * 3)

npMatrix1 = np.array([npArray, npArray, npArray])
npMatrix2 = np.array([aList, aList, aList])
npMatrix3 = np.array([npArray, [1, 1, 1, 1, 1], npArray])
print(npMatrix1)
print(npMatrix2)
print(npMatrix3)

okMatrix = np.array([[1, 2], [3, 4]])
badMatrix = np.array([[1, 2], [1, 2, 3]], dtype=object)
print(okMatrix)
print(badMatrix)
print(okMatrix * 2)
print(badMatrix * 2)

result1 = okMatrix * 2 + 1
print(result1)
result1 = okMatrix + okMatrix
print(result1)
result2 = okMatrix - okMatrix
print(result2)
result1 = okMatrix * okMatrix
print(result1)

matrix = np.array([[1, 2], [3, 4], [5, 6]])
matrixTranspose = matrix.T
print(matrix)
print(matrixTranspose)
matrix1D = np.array([1, 2, 3, 4])
matrix1DTranspose = matrix1D.T
print(matrix1D)
print(matrix1DTranspose)
matrix1x4 = np.array([[1, 2, 3, 4]])
matrix1x4Transpose = matrix1x4.T
print(matrix1x4)
print(matrix1x4Transpose)

# normal = 1ton sigma sqrt(sum(array's element ** 2))
# norm is sqrt of dot product of vector with itself
npArray1 = np.array([1, 2, 3, 4])
npArray2 = np.array([[1, 2], [3, 4]])
print(np.linalg.norm(npArray1))
print(np.linalg.norm(npArray2))
print(np.linalg.norm(npArray2, axis=0))  # column wise normal
print(np.linalg.norm(npArray2, axis=1))  # row wise normal

# dot product => a.b = 1ton sigma sum(ai*bi)
npArray1 = np.array([0, 1, 2, 3])
npArray2 = np.array([4, 5, 6, 7])
print(np.dot(npArray1, npArray2))
print(np.sum(npArray1*npArray2))
print(npArray1 @ npArray2)
sum = 0
for a, b in zip(npArray1, npArray2):
    sum += a*b
print(sum)
print(np.dot(np.array([1, 2]), np.array([3, 4])))
print(np.dot([1, 2], [3, 4]))
# print(np.dot([1, 2], [1, 2, 3])) error

npArray2 = np.array([[1, -1], [2, -2], [3, -3]])
sumByCols = np.sum(npArray2, axis=0)
sumByRows = np.sum(npArray2, axis=1)
print(sumByCols)
print(sumByRows)

# mean => sum of all / number of all
mean = np.mean(npArray2)
meanCols = np.mean(npArray2, axis=0)
meanRows = np.mean(npArray2, axis=1)
print(mean)
print(meanCols)
print(meanRows)

# center the matrix => find mean of cols and substract them from matrix, sum of cols of centered matrix is always 0 and new mean by cols will be 0
# process is not same for rows, for rows first create Transpose then fine centered
centered = npArray2 - np.mean(npArray2, axis=0)
print(centered)
print(np.sum(centered, axis=0))
npArray2 = np.array([[1, 3], [2, 4], [3, 5]])  # Define a 3 x 2 matrix.
# Remove the mean for each row
npArrayCentered = npArray2.T - np.mean(npArray2, axis=1)
npArrayCentered = npArrayCentered.T  # Transpose back the result
print('Original matrix')
print(npArray2)
print('Centered by columns matrix')
print(npArrayCentered)
print('New mean by rows')
print(npArrayCentered.mean(axis=1))

# exercise
npArray3x2 = np.array([[1, 2, 3], [4, 5, 6]])
npArray2x3 = np.array([[1, 2], [3, 4], [4, 5]])
print(npArray3x2)
print(npArray2x3)

npArray3x2 = np.random.randint(1, 10, size=[3, 2])
npArray2x3 = np.random.randint(1, 10, size=[2, 3])
print(npArray3x2)
print(npArray2x3)

print(np.multiply(npArray3x2, npArray2x3.T))
print(np.multiply(npArray3x2.T, npArray2x3))
print(np.matmul(npArray2x3, npArray3x2))
print(np.matmul(npArray3x2, npArray2x3))
print(np.mean(npArray3x2))
