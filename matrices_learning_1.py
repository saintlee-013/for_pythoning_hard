r1, c1 = map(int, input("enter row and column for first matrix\t").split())
r2, c2  = map(int,input("enter row and column for second matrix\t").split())
matrix1 = [[0 for j in range(c1)] for i in range(r1)]
matrix2 = [[0 for j in range(c2)] for i in range(r2)]
matrix3 = [[0 for j in range(c1)] for i in range(r1)]
for i in range(r1):
    for j in range(c1):
        matrix1[i][j] = int(input(f"enter {i,j}\t"))
for i in range(r2):
    for j in range(c2):
        matrix2[i][j] = int(input(f"enter {i,j}\t"))
print("matrix A is")
for i in range(2):
    for j in range(2):
        print(matrix1[i][j], end = " ")
    print("")
print("matrix B is")
for i in range(2):
    for j in range(2):
        print(matrix2[i][j], end = " ")
    print("")
for i in range(0,2):
    for j in range(0,2):
      element = matrix1[i][j] + matrix2[i][j]
      matrix3[i][j]= element
print(matrix3)
for i in range(2):
    for j in range(2):
        print(matrix3[i][j], end = " ")
    print("")
