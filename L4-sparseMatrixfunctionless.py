print("Jithendra-121910313053")
matrix=[[2, 0, 0, 0],
        [3, 0, 5, 0],
        [0, 0, 7, 0],
        [0, 4, 0, 5]]
for i in matrix:
    for j in i:
        print(j, end=" ")
    print()
sparseMatrix=[]
for i in range(len(matrix)):
    for j in range(len(matrix[2])):
        if matrix[i][j]!=0:
            temp=[]
            temp.append(i)
            temp.append(j)
            temp.append(matrix[i][j])
            sparseMatrix.append(temp)
print("\nsparsematrix:")            
for i in sparseMatrix:
    for j in i:
        print(j, end=" ")
    print()            
            
            
