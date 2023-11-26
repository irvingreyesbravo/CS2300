#
# Programing Assignment 2, Part A2
# Name: Irving Reyes Bravo
# Date: 10/26/2023
#

import numpy as np


# declare matrix A
matrixA = np.array([[1, -1, -1, 1],
                    [2, -3, -5, 4],
                    [-2, -1, -2, 2],
                    [3, -3, -1, 2]])
# declare inverse matrix A with rounded values
inverseA = np.linalg.inv(matrixA)
inverseA = np.round(inverseA)
roundedA = inverseA.astype(int)

# declare list to hold matrices values
cypherMatrix = []

# declare matrix row constant
rows = 4

# call function to read linear sequence of numbers from given file
file = open("input-A22.txt", "r")
text = file.readline()

# split incoming line into sequence of numbers
numbers = text.split()
sequence = [int(num) for num in numbers]

# while-loop that will append empty cells with zero
while len(sequence) % rows != 0:
    sequence.append(0)

# declare cypher matrix into appropriately sized column vectors
cipherMatrix = [sequence[element: element + rows] for element in range(0, len(sequence), rows)]
cipherMatrix = np.array(cipherMatrix)
transposeC = cipherMatrix.transpose()

# display cypher matrix
print("Cypher Matrix:")
print(transposeC)

# declare and display variable to hold matrix C
C = np.dot(roundedA, transposeC)
rowsC = len(C)
colsC = len(C[0])
print(C)

# declare variable to hold decrypted message
plainText = ''
# for-loop that iterates through every row in Matrix C
for col in range(colsC):
    # for-loop that iterates through every column in Matrix C
    for row in range(rowsC):
        number = C[row][col]
        # if-statement that quits appending to message when EOF
        if number == 0:
            break
        plainText += chr(number)

# display the decoded message
print("Decoded Message:")
print(plainText)
