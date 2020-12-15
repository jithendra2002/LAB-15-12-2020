print('''Jithendra
121910313053''')
def printing_matrix(m):
    for i in m:
        for j in i:
            print(j, end = " \t")
        print()
n = int(input('Enter the number of rows: '))
m = int(input('Enter the number of coloumns: '))
print('Input the elements of the array : ')
x = []
for i in range(0,n):
    a =[]
    print(f'Enter the value of {i}th row')
    for j in range(0,m):
        a.append(int(input()))
    x.append(a)
print('The original matrix :')
printing_matrix(x)
q=int(input("Enter a threshold value"))
for i in range(len(x)):
    for j in range(len(x[0])):
        if x[i][j]==q:
            x[i][j]=0
print("matrix after taking threshold value")
printing_matrix(x)
sparse_matrix = []
for i in range(len(x)):
    for j in range(len(x[0])):
         if x[i][j] != 0 :
            temp = []
            temp.append(i)
            temp.append(j)
            temp.append(x[i][j])
            sparse_matrix.append(temp)      
print(''''Sparse matrix representation :
Row\tCOl\tValue''')
printing_matrix(sparse_matrix)
        

        

