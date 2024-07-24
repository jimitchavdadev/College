def multiply_matrices(matrix1, matrix2, m, n, p):
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(p)] for _ in range(m)]

    # Perform matrix multiplication
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

def print_matrix(matrix):
    # Print the matrix
    for row in matrix:
        print(' '.join(map(str, row)))

def main():
    # Input dimensions for the matrices
    m = int(input("Enter the number of rows for matrix A: "))
    n = int(input("Enter the number of columns for matrix A (and rows for matrix B): "))
    p = int(input("Enter the number of columns for matrix B: "))

    # Input elements for the first matrix (m x n)
    print("Enter elements of matrix A (row by row):")
    matrix1 = []
    for i in range(m):
        row = list(map(int, input().split()))
        matrix1.append(row)
    
    # Input elements for the second matrix (n x p)
    print("Enter elements of matrix B (row by row):")
    matrix2 = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix2.append(row)
    
    # Multiply matrices
    result = multiply_matrices(matrix1, matrix2, m, n, p)
    
    # Print the result
    print("Resultant matrix:")
    print_matrix(result)

if __name__ == "__main__":
    main()
