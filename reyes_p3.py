#
# Programing Assignment 1, Part A3
# Name: Irving Reyes Bravo
# Date: 09/20/2023
#

# the Science Excel Center helped me in automating the matrix mapping process,
#   but I used my own knowledge of try and except statements to create the function
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


# define function to multiply matrices together and return product
def multiplyMatrices(A, B):
    # if-statement that returns nothing if matrices cannot be multiplied
    if len(A[0]) != len(B):
        return None

    # declare variable to hold product of matrices
    product = []
    # for-loops that iterates through both matrices and enter new value into product matrix
    for m in range(len(A)):
        new = []
        for n in range(len(B[0])):
            # declare variable to store multiplied int value from matrices
            cell = sum(int(A[m][k] * B[k][n]) for k in range(len(A[0])))
            new.append(cell)
        # call method to enter new value into returning matrix
        product.append(new)
    return product


# for-loops that iterate through all combinations of the 4 incoming matrices
for i in range(1, 5):
    for j in range(1, 5):
        # if-statement that stops same-named files from being multiplied
        if i != j:
            # declare variables to hold incoming files and output file
            inputA = f"reyes_mat{i}.txt"
            inputB = f"reyes_mat{j}.txt"
            outputC = f"reyes_p3_out{i}{j}.txt"

            # declare variables to store read-in matrix returned by method
            matrixA = matrixFromFile(inputA)
            matrixB = matrixFromFile(inputB)

            # if-statement that operates matrices if they're present (!= None)
            if matrixA and matrixB:
                # declare variable to store product matrix returned by method
                matrixC = multiplyMatrices(matrixA, matrixB)

                # if-statement that prints matrix to output file if it's present
                if matrixC:
                    # method that writes matrix A * B (or C) to output file
                    with open(outputC, "w") as file:
                        for row in matrixC:
                            file.write("\t".join(map(str, row)) + "\n")

                    # display to user what file the output was saved to
                    print(f"{inputA} * {inputB} has been printed to {outputC}")
                # else (dimensions mismatch) the user is told to enter compatible matrices
                else:
                    print(f"Matrix dimensions mismatch; {inputA} and {inputB} cannot be multiplied.")
            # else (files not found) the user is told to have the correct files
            else:
                print(f"{inputA} or {inputB} could not be found")
