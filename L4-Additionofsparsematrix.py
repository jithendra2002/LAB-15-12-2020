# Addition of two Sparse matrices
print('''Jithendra
121910313053''')
n = int(input('Enter the value of N in NxN matrix: '))

print('''\nThis is a Sparse matrix.
So input high frequency of zeros.''')
#Inputing the first matrix:
print("\nEnter the values for the first matrix : ")

a= []
for i in range(n):
    print(f'Enter the values for {i}th row : ')
    x=[]
    for j in range(n):
      x.append(int(input()))
    a.append(x)

# Inputing the second Matrix:
print('\nEnter the values for the Second Matrix :')
b =[]
for i in range(n):
    print(f'Enter the values for {i}th row : ')
    x=[]
    for j in range (n):
        x.append(int(input()))
    b.append(x)

#Addition of the two matrices:
    
#Creating an empty matrix for storing the value of a + b matrices
s = [[0 for j in range(n)]for i in range(n)]

for i in range(len(a)):
    for j in range(len(a[0])):
        s[i][j] = a[i][j] + b[i][j]

print('The sum of the two sparse matrices is :')
for r in s:
    for y in r:
        print(y, end = " ")
    print()
        
#Converting the Sum of sparse matrices into the sparse matrice representation:
sparse_matrix = []
for i in range(len(s)):
    for j in range(len(s[0])):
        if s[i][j] != 0 :
            temp = []
            temp.append(i)
            temp.append(j)
            temp.append(s[i][j])
            sparse_matrix.append(temp)

print('''The Sparse Matrix representation :
Row\tCol\tValue''')
for i in sparse_matrix:
    for j in i:
        print(j,end = ' \t ')
    print()
