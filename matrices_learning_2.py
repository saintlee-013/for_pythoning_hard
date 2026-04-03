# matrix multiplication
r1,c1 = map(int, input("Enter the row, col for matrix A\t").split())
r2,c2 = map(int,input("Enter the row,col for matrix B\t").split())
matrixA = [[0 for j in range(c1)] for i in range(r1)]
matrixB = [[0 for j in range(c2)] for i in range(r2)]
matrixC = [[0 for j in range(c2)] for i in range(r1)]
if(c1 == r2):
    print("enter A")
    for i in range(r1):
       for j in range(c1):
           matrixA[i][j] = int(input(f"enter {i,j}\t"))
    print("enter B:")
    for i in range(r1):
       for j in range(c1):
           matrixB[i][j] = int(input(f"enter {i,j}\t"))
    print("A is")
    for i in range(r1):
          for j in range(c1):
           print(matrixA[i][j], end = " ")
          print("")
    print("B is")
    for i in range(r1):
          for j in range(c1):
              print(matrixB[i][j], end = " ")
          print("")
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
             matrixC[i][j] = matrixC[i][j] + (matrixA[i][k]*matrixB[k][j])
    print("resultant is")
    for i in range(r1):
          for j in range(c2):
              print(matrixC[i][j], end = " ")
          print("")



else:
    print("not possible")
