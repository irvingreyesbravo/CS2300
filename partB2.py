#
# Programing Assignment 2, Part B
# Name: Irving Reyes Bravo
# Date: 10/27/2023
#

import numpy as np


# Part B2.1
# declare input flow numbers (cast as floats)
flow1 = float(input("Enter Flow 1: "))
flow2 = float(input("Enter Flow 2: "))
flow3 = float(input("Enter Flow 3: "))
flow4 = float(input("Enter Flow 4: "))

# declare the augmented matrix
A = np.array([
    [1, 1, 0, 0, flow1],
    [1, 0, 0, 1, flow2],
    [0, 1, 1, 0, flow3],
    [0, 0, 1, 1, flow4]],
    dtype=float)

# display augmented matrix with format
print("Augmented Matrix:")
np.set_printoptions(precision=2, suppress=True)
print(A)


# Part B2.2
# define variable to hold num of rows in augmented matrix
rowsA = A.shape[0]

# for loop that iterates through augmented matrix
for i in range(rowsA):
    # declare pivot row and append value while traversing rows in A
    pivotRow = i
    while pivotRow < rowsA and A[pivotRow, i] == 0:
        pivotRow += 1

    # if-statement that continues to next column if not pivot is found
    if pivotRow == rowsA:
        continue

    # swap current row with the piot-containing row
    A[i], A[pivotRow] = A[pivotRow].copy(), A[i].copy()
    # normalize pivot row
    A[i] /= A[i, i]

    # for-loop that iterates through the rest of the columns
    for j in range(rowsA):
        # if-statement that decrements remaining elements to zero
        if j != i:
            A[j] -= A[j, i] * A[i]

# display the resulting matrix
print("\nResulting Matrix:")
print(A)
