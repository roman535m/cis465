#Roman Melnik - 2693934
#CIS 465 - Professor Essa
#Assignment 1 - Part 1

#padding the matrix with zero's
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
    rows = 9
    columns = 9

    matrix = []
    pad_matrix(n=9, matrix=matrix)
    pad_matrix(matrix=matrix, l=[0, 3, 2, 5, 4, 7, 6, 9, 8])
    pad_matrix(matrix=matrix, l=[3, 0, 1, 2, 3, 4, 5, 6, 7])
    pad_matrix(matrix=matrix, l=[2, 1, 0, 3, 2, 5, 4, 7, 6])
    pad_matrix(matrix=matrix, l=[5, 2, 3, 0, 1, 2, 3, 4, 5])
    pad_matrix(matrix=matrix, l=[4, 3, 2, 1, 0, 3, 2, 5, 4])
    pad_matrix(matrix=matrix, l=[7, 4, 5, 2, 3, 0, 1, 2, 3])
    pad_matrix(matrix=matrix, l=[6, 5, 4, 3, 2, 1, 0, 3, 2])
    pad_matrix(matrix=matrix, l=[9, 6, 7, 4, 5, 2, 3, 0, 1])
    pad_matrix(matrix=matrix, l=[8, 7, 6, 5, 4, 3, 2, 1, 0])
    pad_matrix(matrix=matrix, n=9)

    #display the original matrix
    print("Matrix to process: ")
    for i in matrix:
        print(i)

    answer = []
    for i in range(1, rows + 1):
        myRow = []
        for j in range(1, columns + 1):

            currentPosition = matrix[i][j]

            #performing step 1 of the 6 step process
            rightValue = matrix[i][j + 1] - currentPosition
            topRightValue = matrix[i - 1][j + 1] - currentPosition
            topValue = matrix[i - 1][j] - currentPosition
            topLeftValue = matrix[i - 1][j - 1] - currentPosition
            leftValue = matrix[i][j - 1] - currentPosition
            bottomLeftValue = matrix[i + 1][j - 1] - currentPosition
            bottomValue = matrix[i + 1][j] - currentPosition
            bottomRightValue = matrix[i + 1][j + 1] - currentPosition

            #performing steps 2, 3, and 4 of the 6 step process
            #if else statements check if the value is positive or negative
            #if the value is positive, the value should be reassigned to one
            #however, we skip this step and reassign the value to the corresponding decimal value
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

            #step 5
            #here we add the value of the neighbors and substitue it for the element of interest by appending to the myRow list
            sum = rightValue + topRightValue + topValue + topLeftValue + leftValue + bottomLeftValue + bottomValue + bottomRightValue
            myRow.append(sum)
        #myRow gets appended to the answer list
        answer.append(myRow)
    #display the final result
    print("\nResult: ")
    for row in answer:
        print(row)

if __name__ == '__main__':
    main()