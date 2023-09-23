#
# Programing Assignment 1, Part A1
# Name: Irving Reyes Bravo
# Date: 09/20/2023
#


# declare variables to hold first and last names
firstName = "Irving"
lastName = "Reyes"

# declare two sets of rows and columns based off of string's lengths
mat1Rows = len(lastName)
mat1Cols = len(firstName)
mat2Rows = len(lastName)
mat2Cols = len(firstName)

# initialize first two matrices as empty lists based on the declared rows and cols
mat1 = [[0] * mat1Cols for _ in range(mat1Rows)]
mat2 = [[0] * mat2Cols for _ in range(mat2Rows)]
# initialize next two matrices as empty lists based on set rows and cols
mat3 = [[0, 0, 0, 0], [0, 0, 0, 0]]
mat4 = [[0, 0], [0, 0], [0, 0], [0, 0]]

# fill matrix 1 with defined value
value1st = 1
# for-loops to iterate over columns then over rows
for col in range(mat1Cols):
    for row in range(mat1Rows):
        mat1[row][col] = value1st
        # increment matrix value by given set value
        value1st += 1

# fill matrix 2 with defined value
value2nd = 2
# for-loops to iterate over rows then over columns
for row in range(mat2Rows):
    for col in range(mat2Cols):
        mat2[row][col] = value2nd
        # increment matrix value by given set value
        value2nd += 3

# fill matrix 3 with defined value
value3rd = 10
# for-loops to iterate over columns then over rows
for col in range(4):
    for row in range(2):
        mat3[row][col] = value3rd
        # increment matrix value by given set value
        value3rd += -2

# fill matrix 4 with defined values
value4th = -6
# for-loops to iterate over rows then over columns
for row in range(4):
    for col in range(2):
        mat4[row][col] = value4th
        # increment matrix value by given set value
        value4th += 1.5

# declare list variable to hold matrix file names
files = ["reyes_mat1.txt",
         "reyes_mat2.txt",
         "reyes_mat3.txt",
         "reyes_mat4.txt"]

# for-loop that iterates through the index of every matrix
for i, mat in enumerate([mat1, mat2, mat3, mat4]):
    fileName = files[i]
    # method that reads matrix from input file
    with open(fileName, "w") as file:
        for row in mat:
            file.write("\t".join(map(str, row)) + "\n")

# for-loop that prints through the matrix of every file
for i, fileName in enumerate(files):
    print(f"Matrix {i + 1} has been printed to {fileName}")
