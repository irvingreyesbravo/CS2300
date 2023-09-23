#
# Programing Assignment 1, Part B5
# Name: Irving Reyes Bravo
# Date: 09/22/2023
#

# define function that calculates dot product of two vectors and returns it
def dotProduct(vector1, vector2):
    return sum(vector1[i][0] * vector2[i][0] for i in range(len(vector1)))


# the Science Excel Center also helped me in displaying my vectors as ints not floats
# declare list variable to hold (2x1) vectors with int values
vectorList = {'r': [[-1], [-2]],
              's': [[-3], [3]],
              'u': [[2], [-1]],
              'v': [[3], [1]],
              'w': [[1], [3]]}

# declare variable to prompt for incoming vector name from user
print(f"Vectors: {vectorList}")
inVectorA = input("Enter the name of the first vector:\n")
inVectorB = input("Enter the name of the second vector:\n")

# if-statement that operates if vector names entered are in vector list
if inVectorA in vectorList and inVectorB in vectorList:
    # declare variables to store chosen vectors
    vectorA = vectorList[inVectorA]
    vectorB = vectorList[inVectorB]

    # declare variable to store read-in vector returned by method
    product = dotProduct(vectorA, vectorB)

    # declare variable to hold output file for dot product
    productFile = f"reyes_p5_out{inVectorA}{inVectorB}.txt"
    # method that writes product from A * B (or C) to output file
    with open(productFile, "w") as outFile:
        outFile.write(str(product))

    # display to user what file the output was saved to
    print(f"{inVectorA} * {inVectorB} has been printed to {productFile}")
# else (names are invalid) the program halts
else:
    print("Sorry! Invalid vector name entered.")
