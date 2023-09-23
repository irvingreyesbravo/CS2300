#
# Programing Assignment 1, Part A4
# Name: Irving Reyes Bravo
# Date: 09/20/2023
#

import numpy as np


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


# for-loops that iterate through all combinations of the 4 incoming matrices
for i in range(1, 5):
    for j in range(1, 5):
        # if-statement that stops same-named files from being multiplied
        if i != j:
            # declare variables to hold incoming files
            inputA = f"reyes_mat{i}.txt"
            inputB = f"reyes_mat{j}.txt"
            # declare variables to hold output files for both operations
            addOutput = f"reyes_p4_outA{i}{j}.txt"
            multOutput = f"reyes_p4_outM{i}{j}.txt"

            # declare variables to store read-in matrix returned by method
            matrixA = matrixFromFile(inputA)
            matrixB = matrixFromFile(inputB)

            # if-statement that operates matrices if they're present (!= None)
            if matrixA and matrixB:
                # declare variables that checks whether matrices can be added or multiplied
                canAdd = np.array(matrixA).shape == np.array(matrixB).shape
                canMultiply = np.array(matrixA).shape[1] == np.array(matrixB).shape[0]

                # if-statement that performs matrix addition on compatible matrices
                if canAdd:
                    # declare variable to hold matrix returned by np library
                    addMatrix = np.add(matrixA, matrixB).astype(int)

                    # call method that prints the incoming matrix to its operand output
                    matrixToFile(addMatrix, addOutput)
                    print(f"{inputA} + {inputB} has been printed to {addOutput}")
                # else (dimensions mismatch) the user is told to enter compatible matrices
                else:
                    print(f"Matrix dimensions mismatch; {inputA} and {inputB} cannot be added.")

                # if-statement that performs matrix multiplication on compatible matrices
                if canMultiply:
                    # declare variable to hold matrix returned by np library
                    multMatrix = np.dot(matrixA, matrixB).astype(int)

                    # call method that prints the incoming matrix to its operand output
                    matrixToFile(multMatrix, multOutput)
                    print(f"{inputA} * {inputB} has been printed to {multOutput}")
                # else (dimensions mismatch) the user is told to enter compatible matrices
                else:
                    print(f"Matrix dimensions mismatch; {inputA} and {inputB} cannot be multiplied.")
            # else (files not found) the user is told to have the correct files
            else:
                print(f"{inputA} or {inputB} could not be found")
