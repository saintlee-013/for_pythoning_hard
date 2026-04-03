m = []
n = int(input())
t = int(input())
for i in range(0,n):
    row = []
    for j in range(0,n):
        row = int(input())
        m.append(row)
for i in range(0,n):
    for j in range(0,n):
        print(int(m[i][j]))
