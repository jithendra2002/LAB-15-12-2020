print("jithendra naidu-121910313053")
def printing_matrix(matrix) :
    for i in matrix:
        for j in i:
            print(j, end =" ")
        print()
    
matrix=[[2,0,0,0],
        [9,0,7,0],
        [0,0,5,0],
        [0,4,0,6]]
print('Input Matrix : ')

printing_matrix(matrix)
sparseMatrix=[]
for i in range(len(matrix)):
    for j in range(len(matrix[1])):
        if matrix[i][j]!=0:
            temp=[]
            temp.append(i)
            temp.append(j)
            temp.append(matrix[i][j])
            sparseMatrix.append(temp)
print("\nsparsematrix:")

printing_matrix(sparseMatrix)
