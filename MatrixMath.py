def buildMatrix():
    coord = input('Enter size of matrix: ').split()
    coord = [int(val) for val in coord] 
    row, col = coord
    matrix = []

    print('Please define matrix: ') 
    for i in range(row): 
        newRow = input().split()
        newRow = [float(num) for num in newRow]
        matrix.append(newRow)

    return [row, col, matrix]


def scaleMatrix(matrix=[], const=None):
    if matrix == []:
        row, col, mat = buildMatrix()
    else: 
        row, col, mat = matrix
        
    if const == None: 
        const = float(input('Enter constant: '))
        
    matrixC = []
    
    for i in range(row):
        matrixC.append([])
        for j in range(col):
                matrixC[i].append(mat[i][j] * const)
                
    return matrixC


def addMatrix():
    aRow, aCol, matA = buildMatrix()
    bRow, bCol, matB = buildMatrix()
    matC = []

    if (aRow == bRow and aCol == bCol):
        for i in range(aRow):
            matC.append([])
            for j in range (aCol):
                matC[i].append(matA[i][j] + matB[i][j])

        return matC
    else:
        print('The operation cannot be performed.\n')


def transposeMatrix(matrix, choice=1):
    row, col, matrix = matrix
    
    if choice == 4:
        matrix.reverse()
        return matrix        
    elif choice == 3:
        for i in range(row):
            matrix[i].reverse()            
        return matrix       
    else:
        inverted = []
        
        for i in range(col) if choice == 1 else range(col - 1, -1, -1):
            chunk = []
            for j in range(row) if choice == 1 else range(row - 1, -1, -1):
                chunk.append(matrix[j][i])
            inverted.append(chunk)
            
        return inverted

               
def multiplyMatrix():
    aRow, aCol, matA = buildMatrix()
    
    matB = buildMatrix()
    inverseB = transposeMatrix(matB)
    bRow, bCol, matB = matB
   
    matC = []
    
    if aCol == bRow:
        for i in range(aRow):
            matC.append([])
            for j in range(bCol):
                unitPoint = 0
                chunk = matA[i]
                for k in range(aCol):
                    unitPoint += chunk[k] * inverseB[j][k]

                matC[i].append(unitPoint)
                
        return matC
    
    else:
        print('The operation cannot be performed.\n')


def findMinor(i, j, matrix):
    row, col, working_matrix = matrix
    working_matrix = transposeMatrix([row, col, working_matrix])
    del working_matrix[j]
    working_matrix = transposeMatrix([row - 1, col, working_matrix])
    del working_matrix[i]
    return working_matrix


def findDeterminant(matrix):
    row, col, matrix = matrix
    detMinor = [] 
    if row == col:
        if row == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        elif row == 1:
            return matrix[0][0]
        else:
            for j in range(row):
                detMinor.append(pow(-1, j) * (matrix[0][j] * findDeterminant([len(matrix) - 1, len(matrix) - 1, findMinor(0, j, [row, col, matrix])])))

            return sum(detMinor)
    else:
        return 'Matrix must be square'


def inverseMatrix():
    row, col, matrix = buildMatrix()
    determinant = findDeterminant([row, col, matrix])
    adjoint = []
    if determinant == 0:
        print('Inverse does not exit')
    else:
        for i in range(row):
            adjoint.append([])
            for j in range(row):
                adjoint[i].append(pow(-1, i + j) * (findDeterminant([len(matrix) - 1, len(matrix) - 1, findMinor(i, j, [row, col, matrix])])))
        transposed = transposeMatrix([row, col, adjoint])
        return scaleMatrix([row, col, transposed], 1 / determinant)


def printMatrix(matrix):
    if matrix:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = str(matrix[i][j])

        print('The result is: ') 
        for i in range(len(matrix)):
            print(' '.join(matrix[i]))
        print()
    else:
        pass


def main():
    choice = True
    while choice != 0:
        print('''
1. Add matrices
2. Multiply matrix by a constant
3. Multiple matrices
4. Transpose matrices
5. Calculate the determinant
6. Inverse matrix
0. Exit''')
        choice = int(input('Your choice: '))
        if choice == 1:
            printMatrix(addMatrix())
        elif choice == 2:
            printMatrix(scaleMatrix())
        elif choice == 3:
            printMatrix(multiplyMatrix())
        elif(choice == 4):
            print('''
1. Main Diagonal
2. Side Diagonal
3. Vertical line
4. Horizontal line''')
            choice = int(input('Your choice: '))
            printMatrix(transposeMatrix(buildMatrix(), choice))
        elif(choice == 5):
            print('The result is:\n' + str(findDeterminant(buildMatrix())))
        elif(choice == 6):
            printMatrix(inverseMatrix()) 
        else:
            # print('Please make valid selection')
            pass


main()
