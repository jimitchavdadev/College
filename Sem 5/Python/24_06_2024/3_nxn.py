matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

n = len(matrix1)
result = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            result[i][j] += matrix1[i][k] * matrix2[k][j]


for row in result:
    print(row)
