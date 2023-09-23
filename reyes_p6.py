#
# Programing Assignment 1, Part B6
# Name: Irving Reyes Bravo
# Date: 09/22/2023
#

# declare list variable to hold incoming matrices
matrixList = ["reyes_mat1.txt",
              "reyes_mat2.txt",
              "reyes_mat3.txt",
              "reyes_mat4.txt"]

# for-loop that iterates throw the matrix (index) of each matrix in the list
for mat, matrixFile in enumerate(matrixList, start=1):
    # method that reads matrix from input file
    with open(matrixFile, "r") as inFile:
        matrix = [list(map(float, line.strip().split("\t"))) for line in inFile]

    # declare variable to store transposed matrix (switch row and col values)
    matrixTransposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    # declare variable to hold output file for transposed matrix
    transposeFile = f"reyes_p6_mat{mat}.txt"
    # method that writes transposed matrix to output file
    with open(transposeFile, "w") as outFile:
        for row in matrixTransposed:
            outFile.write("\t".join(map(str, row)) + "\n")

    # display to user what file the output was saved to
    print(f"The transpose of {matrixFile} has been printed to {matrixTransposed}")
