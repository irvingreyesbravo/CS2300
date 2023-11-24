#
# Programing Assignment 3, Part 1
# Name: Irving Reyes Bravo
# Date: 11/23/2023
#

import numpy as np


# define function that reads in both matrices from a file
def readInMatrix(filePath):
    # call funtion to read lines from the incoming file path
    with open(filePath, 'r') as file:
        lines = file.readlines()
        # parse the first three lines as matrix "D"
        matrixInOut = [list(map(float, line.split())) for line in lines[:3]]
        # parse the next three lines as matrix "E"
        matrixExtDemand = [float(line) for line in lines[3:]]
    return np.array(matrixInOut), np.array(matrixExtDemand)


def main():
    # declare a variable to hold file containing matrices D and E
    inputFile = "inputMatrices.txt"
    # call function and read in matrices D and E
    matrixD, matrixE = readInMatrix(inputFile)

    # declare a variable to hold a (3x3) identity matrix
    matrixI = np.identity(3)

    # declare a variable to store the inverse matrix (I - D)
    inverseMatrix = np.linalg.inv(matrixI - matrixD)

    # declare a variable to hold the output matrix X using this formula: X = (I - D)^-1 * E
    matrixX = np.dot(inverseMatrix, matrixE)
    # redeclare variable, rounding all elements to the nearest tenth
    matrixX = np.round(matrixX, decimals=1)

    # display matrix X to user
    print("Output Matrix X:")
    print(matrixX)


# main loop is called here
if __name__ == '__main__':
    main()
