#
# Programing Assignment 3, Part 2
# Name: Irving Reyes Bravo
# Date: 11/23/2023
#

import numpy as np
import matplotlib.pyplot as plt


# define function that reads in pairs (x, y) from a file
def readInPairs(filePath):
    # call funtion to read lines from the incoming file path
    with open(filePath, 'r') as file:
        lines = file.readlines()
        # declare a variable to hold new tuple of floats, representing pairs (x, y)
        pair = [tuple(map(float, line.split())) for line in lines]
    return np.array(pair)


# define function that performs the matrix form for linear regression
def leastSquaresReg(pair):
    # declare variables to hold incoming pairs (x, y), adding a column of ones for the intercept form
    X = np.c_[np.ones(pair.shape[0]), pair[:, 0]]
    Y = pair[:, 1]

    # declare and calculate the coefficients of the least squares regression line
    A = np.linalg.inv(X.T @ X) @ X.T @ Y
    return A


# define function that plots the points and regression line
def plotRegLine(pair, data):
    # declare variables to hold the incoming pairs (x, y)
    x, y = pair[:, 0], pair[:, 1]
    # call method and plot the given data points
    plt.scatter(x, y, color='blue', label='Data Points')

    # declare and calculate regression line using the linear function
    regLine = data[0] + data[1] * x
    # call method and plot the regression line
    plt.plot(x, regLine, color='red', label=f'Regression Line: y = {data[1]:.2f}x + {data[0]:.2f}')

    # call methods for proper labeling and formatting
    plt.xlabel('Price ($)')
    plt.ylabel('Monthly Sales')
    plt.legend()
    plt.title('Least Squares Regression Analysis')
    plt.grid(True)
    plt.show()


def main():
    # declare variable to hold file containing data points
    inputFile = "dataPoints.txt"

    # call method to read data from the input file
    data = readInPairs(inputFile)
    # call method to perform the least squares regression
    coefficients = leastSquaresReg(data)

    # display the linear equation to the user
    print(f"Linear Equation: y = {coefficients[1]:.1f}x + {coefficients[0]:.1f}")
    # call method and plot the data points and the regression line
    plotRegLine(data, coefficients)


# main loop is called here
if __name__ == '__main__':
    main()
