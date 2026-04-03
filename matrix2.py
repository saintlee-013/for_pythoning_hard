# matrix multiplications using functions
list_of_matrix = []
def inputs_matrix():
    rows = int(input("Enter the number of rows: "))
    col = int(input("Enter the number of columns: "))
    M = [[0 for j in range(col)] for i in range(rows)]
    
    print(f"Enter the {rows}x{col} matrix elements:")
    for i in range(rows):
        for j in range(col):
            M[i][j] = int(input(f"Enter element at [{i}][{j}]: ")) 
    return M

no_of_matrix = int(input("Enter the number of matrixes\t"))
for i in range(no_of_matrix):
 final_matrix = inputs_matrix()
 list_of_matrix.append(final_matrix)
 print("\nYour final matrix is:")
 for row in final_matrix:
     print(row)
print(list_of_matrix) 

