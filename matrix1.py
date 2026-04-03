# matrix multiplication wihout using functions 
row_A = int(input(f"The row number for A\t"))
col_A = int(input(f"The col number for A\t"))
row_B = int(input(f"The row number for B\t"))
col_B = int(input(f"The col number for B\t"))
A = [[0 for j in range(col_A)] for i in range(row_A)]
B = [[0 for j in range(col_B)] for i in range(row_B)]
C = [[0 for j in range(col_B)] for i in range(row_A)]


print("Enter for A")
for i in range(row_A):
    for j in range(col_A):
        A[i][j] = int(input(f"enter element at [{i}][{j}]\t"))
print("Enter for B")
for i in range(row_B):
    for j in range(col_B):
        B[i][j] = int(input(f"enter element at [{i}][{j}]\t"))
print(A)
print(B)
if(col_A==row_B):
    print("allowed\n")
    for i in range(row_A):
        for j in range(col_B):
            for k in range(row_B):
               C[i][j] += (A[i][k])*(B[k][j])
else:
    print("not allowed ")
if(col_A==row_B):
 print(C)
