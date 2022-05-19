#Roman Melnik - 2693934
#CIS 465 - Professor Zhao
#Assignment 1 - Part 2

#padding the matrix with zeroes
def pad_matrix(matrix, n=None, l=None):
    temp = []
    if l is None:
        for i in range(n + 2):
            temp.append(0)
        matrix.append(temp)
    else:
        temp.append(0)
        for j in l:
            temp.append(j)
        temp.append(0)
        matrix.append(temp)

def main():
    #get the matrix size from user
    rows = int(input("Enter # of rows: "))
    columns = int(input("Enter # of columns: "))

    #have user enter values for their matrix
    print("Now it is time to enter", rows*columns, "values for your matrix")
    userMatrix = []
    pad_matrix(n=columns, matrix=userMatrix)
    for i in range(0, rows):
        tempRow = []
        tempRow.append(0) #append a 0 at the beginning of the row for padding
        for j in range(0, columns):
            userInput = int(input("Enter value: "))
            tempRow.append(userInput)
        tempRow.append(0) #append a 0 at the end of the row for padding
        userMatrix.append(tempRow)
    pad_matrix(n=columns, matrix=userMatrix)

    #display the matrix before processing it
    print("Matrix to be processed: ")
    for i in userMatrix:
        print(i)

    #go through steps 1-6
    answer = []
    for i in range(1, rows + 1):
        myRow = []
        for j in range(1, columns + 1):

            currentPosition = userMatrix[i][j]

            rightValue = userMatrix[i][j+1] - currentPosition
            topRightValue = userMatrix[i-1][j+1] - currentPosition
            topValue = userMatrix[i-1][j] - currentPosition
            topLeftValue = userMatrix[i-1][j-1] - currentPosition
            leftValue = userMatrix[i][j-1] - currentPosition
            bottomLeftValue = userMatrix[i+1][j-1] - currentPosition
            bottomValue = userMatrix[i+1][j] - currentPosition
            bottomRightValue = userMatrix[i+1][j+1] - currentPosition

            # performing steps 2, 3, and 4 of the 6 step process
            # if else statements check if the value is positive or negative
            # if the value is positive, the value should be reassigned to one
            # however, we skip this step and reassign the value to the corresponding decimal value
            if rightValue >= 0:
                rightValue = 1
            else:
                rightValue = 0

            if topRightValue >= 0:
                topRightValue = 2
            else:
                topRightValue = 0

            if topValue >= 0:
                topValue = 4
            else:
                topValue = 0

            if topLeftValue >= 0:
                topLeftValue = 8
            else:
                topLeftValue = 0

            if leftValue >= 0:
                leftValue = 16
            else:
                leftValue = 0

            if bottomLeftValue >= 0:
                bottomLeftValue = 32
            else:
                bottomLeftValue = 0

            if bottomValue >= 0:
                bottomValue = 64
            else:
                bottomValue = 0

            if bottomRightValue >= 0:
                bottomRightValue = 128
            else:
                bottomRightValue = 0

            # step 5
            # here we add the value of the neighbors and substitue it for the element of interest by appending to the myRow list
            sum = rightValue + topRightValue + topValue + topLeftValue + leftValue + bottomLeftValue + bottomValue + bottomRightValue
            myRow.append(sum)
        #myRow gets appended to the answer list
        answer.append(myRow)
    #display the final result
    print("\nAnswer: ")
    for row in answer:
        print(row)

if __name__ == '__main__':
    main()