def multiply_matrices(matrix1, matrix2, n):
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(n)] for _ in range(n)]

    # Perform matrix multiplication
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

def print_matrix(matrix):
    # Print the matrix
    for row in matrix:
        print(' '.join(map(str, row)))

def main():
    # Input the size of the matrices
    n = int(input("Enter the size of the matrices (n for n x n): "))

    # Input elements for the first matrix
    print("Enter elements of matrix A (row by row):")
    matrix1 = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix1.append(row)
    
    # Input elements for the second matrix
    print("Enter elements of matrix B (row by row):")
    matrix2 = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix2.append(row)
    
    # Multiply matrices
    result = multiply_matrices(matrix1, matrix2, n)
    
    # Print the result
    print("Resultant matrix:")
    print_matrix(result)

if __name__ == "__main__":
    main()
