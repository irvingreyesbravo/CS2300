#
# Programing Assignment 2, Part A1
# Name: Irving Reyes Bravo
# Date: 10/20/2023
#

import numpy as np


# declare matrix A
matrixA = np.array([[1, -1, -1, 1],
                    [2, -3, -5, 4],
                    [-2, -1, -2, 2],
                    [3, -3, -1, 2]])
# declare inverse matrix A
transposeA = matrixA.transpose()

# declare two lists (B & C) two hold linear sequences
B = []
C = []

# declare hex base and matrx row constants
hexBase = 16
rows = 4

# call function to read in given file
file = open("input-A21.txt", "r")
# declare variable to read in file's content into a list of chars
text = [i for message in file for i in message]

# declare variable to hold extracted plain text, excluding the EOF
plainText = text[0:-1]
# for-loop that iterates through each letter in the plain text
for letter in plainText:
    # convert each letter into its hexadecimal Unicode equivalent
    hexUnicode = hex(ord(letter))
    # extract first hex digit, convert to int, and multiply it by the hex base
    result = int(hexUnicode[2]) * hexBase

    # extract the second hex digit, convert to int, and add it to the result
    tenth = int(hexUnicode[3].upper(), hexBase)
    newASCII = result + tenth

    # append list B with new ASCII value
    B.append(newASCII)

# while-loop that fills empty slots in matrix B with zeroes
while len(B) % rows != 0:
    B.append(0)

# split list B into 'row' lengths to form matrix B
matrixB = [B[element: element + rows] for element in range(0, len(B), rows)]

# calculate transpose of matrix B
matrixB = np.array(matrixB)
transposeB = matrixB.transpose()

# display transpose of matrix B
print("Matrix B:")
print(transposeB)

# display matrix C by performing matrix multiplication
C = np.matmul(matrixA, transposeB)
print("\nMatrix C:")
print(C)
