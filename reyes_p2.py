#
# Programing Assignment 1, Part A2
# Name: Irving Reyes Bravo
# Date: 09/20/2023
#

# declare variables to prompt incoming text files for matrices (A & B) from user
inputA = input("Enter the filename for Matrix A:\n")
inputB = input("Enter the filename for Matrix B:\n")

# extract numbers from incoming matrices and store for file name usage
inputANums = inputA.split("_")[1].split(".")[0]
inputBNums = inputB.split("_")[1].split(".")[0]

# try-statement that will excuse file processing errors
try:
    # method that reads matrix A from input file A
    with open(inputA, "r") as fileA:
        matrixA = [list(map(float, line.strip().split("\t"))) for line in fileA]
    # method that reads matrix B from input file B
    with open(inputB, "r") as fileB:
        matrixB = [list(map(float, line.strip().split("\t"))) for line in fileB]

    # if-statement that checks the dimensions of the incoming values are equal and not empty
    if len(matrixA) != len(matrixB) or len(matrixA[0]) != len(matrixB[0]):
        print("Matrices entered cannot be added (different dimensions).")
    # else (they're fine) the matrices are added together
    else:
        # declare variable to store int-casted operation that adds every corresponding row and column together
        matrixC = [[int(matrixA[i][j] + matrixB[i][j]) for j in range(len(matrixA[0]))] for i in range(len(matrixA))]

        # declare variable to hold output file name based on the matrices sent in
        outputC = f"reyes_p2_out{inputANums}{inputBNums}.txt"
        # method that writes matrix A + B (or C) to output file
        with open(outputC, "w") as output:
            for row in matrixC:
                output.write("\t".join(map(str, row)) + "\n")

        # display to user what file the output was saved to
        print(f"[A + B] has been printed to {outputC}")
# except-statement that reminds user to input correct file names
except FileNotFoundError:
    print("One or both of the files entered could not be found.")
