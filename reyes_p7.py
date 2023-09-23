#
# Programing Assignment 1, Part B7
# Name: Irving Reyes Bravo
# Date: 09/22/2023
#

import numpy as np


# define function to perform dot product using library
def dotProduct(vector1, vector2):
    return np.dot(vector1.flatten(), vector2.flatten())


# define function to perform transpose using library
def findTranspose(matrix):
    return np.transpose(matrix)


# define function to read matrix from incoming file and return it
def matrixFromFile(fileName):
    # try-statement that will excuse file processing error
    try:
        # method that reads matrix from incoming file
        with open(fileName, "r") as inFile:
            matrix = [list(map(float, line.strip().split("\t"))) for line in inFile]
        return matrix
    # except-statement that returns none if files aren't found
    except FileNotFoundError:
        return None


# define function to write matrix to output file
def matrixToFile(matrix, fileName):
    # method that writes incoming matrix to output file
    with open(fileName, "w") as outFile:
        for row in matrix:
            outFile.write("\t".join(map(str, row)) + "\n")


# declare list variable to hold (2x1) vectors with int values
vectorList = {'r': np.array([[-1], [-2]], dtype=int),
              's': np.array([[-3], [3]], dtype=int),
              'u': np.array([[2], [-1]], dtype=int),
              'v': np.array([[3], [1]], dtype=int),
              'w': np.array([[1], [3]], dtype=int)}

# declare variable to prompt for incoming vector name from user
print(f"Vectors: {vectorList}")
inputVector1 = input("Enter the first vector for Dot Product:\n")
inputVector2 = input("Enter the second vector for Dot Product:\n")

# if-statement that operates if vector names entered are in vector list
if inputVector1 in vectorList and inputVector2 in vectorList:
    # declare variables to store chosen vectors
    vectorA = vectorList[inputVector1]
    vectorB = vectorList[inputVector2]

    # declare variable to store read-in vector returned by method
    newProduct = dotProduct(vectorA, vectorB)

    # declare variable to hold output file for dot product
    productFile = f"reyes_p7_outD{inputVector1}{inputVector2}.txt"
    # method that writes product from A * B (or C) to output file
    with open(productFile, "w") as file:
        file.write(str(newProduct))

    # display to user what file the output was saved to
    print(f"Product was printed to {productFile}")
# else (names are invalid) the program halts
else:
    print("Sorry! Invalid vector name entered.")

# declare variable to prompt for incoming matrix number from user
print(f"\nMatrices: 1, 2, 3, or 4")
matrixNum = input("Enter matrix file to read in and transpose:\n")

# if-statement that operates if matrix number entered are in matrix list
if matrixNum in ['1', '2', '3', '4']:
    # declare variable to hold file name of matrix chosen
    matrixToTranspose = f"reyes_mat{matrixNum}.txt"
    originalMatrix = matrixFromFile(matrixToTranspose)
    # declare variable to store transposed matrix (switch row and col values)
    matrixTransposed = findTranspose(originalMatrix)

    # declare variable to hold output file for transposed matrix
    transposedFile = f"reyes_p7_outT{matrixNum}.txt"
    # call method that prints the incoming matrix to its operand output
    matrixToFile(matrixTransposed, transposedFile)
    print(f"The transpose of Matrix {matrixNum} has been printed to {transposedFile}")
# else (number is invalid) the program halts
else:
    print("Sorry! Invalid matrix file name entered.")
