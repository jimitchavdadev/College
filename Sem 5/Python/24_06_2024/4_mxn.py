matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix2 = [
    [7, 8],
    [9, 10],
    [11, 12]
]

m = len(matrix1)
n = len(matrix1[0])

n2 = len(matrix2)
p = len(matrix2[0])

if n != n2:
    raise ValueError("columns in matrix1 not equal to number of rows in matrix2")

# result matrix
result = [[0] * p for _ in range(m)]

for i in range(m):
    for j in range(p):
        for k in range(n):
            result[i][j] += matrix1[i][k] * matrix2[k][j]


for row in result:
    print(row)
