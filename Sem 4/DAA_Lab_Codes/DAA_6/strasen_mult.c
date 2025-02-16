#include <stdio.h>
#include <stdlib.h>
 
// Function to add two matrices
void matrixAddition(int n, int A[][n], int B[][n], int C[][n]) {
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            C[i][j] = A[i][j] + B[i][j];
}
 
// Function to subtract two matrices
void matrixSubtraction(int n, int A[][n], int B[][n], int C[][n]) {
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            C[i][j] = A[i][j] - B[i][j];
}
 
// Function to multiply two matrices using Strassen algorithm
void strassen(int n, int A[][n], int B[][n], int C[][n]) {
    if (n == 1) {
        C[0][0] = A[0][0] * B[0][0];
        return;
    }
 
    int newSize = n / 2;
    int A11[newSize][newSize], A12[newSize][newSize], A21[newSize][newSize], A22[newSize][newSize];
    int B11[newSize][newSize], B12[newSize][newSize], B21[newSize][newSize], B22[newSize][newSize];
    int C11[newSize][newSize], C12[newSize][newSize], C21[newSize][newSize], C22[newSize][newSize];
    int M1[newSize][newSize], M2[newSize][newSize], M3[newSize][newSize], M4[newSize][newSize];
    int M5[newSize][newSize], M6[newSize][newSize], M7[newSize][newSize];
    int temp1[newSize][newSize], temp2[newSize][newSize];
 
    // Divide matrices A and B into submatrices
    for (int i = 0; i < newSize; i++) {
        for (int j = 0; j < newSize; j++) {
            A11[i][j] = A[i][j];
            A12[i][j] = A[i][j + newSize];
            A21[i][j] = A[i + newSize][j];
            A22[i][j] = A[i + newSize][j + newSize];
            B11[i][j] = B[i][j];
            B12[i][j] = B[i][j + newSize];
            B21[i][j] = B[i + newSize][j];
            B22[i][j] = B[i + newSize][j + newSize];
        }
    }
 
    // Calculating M1 to M7
    matrixAddition(newSize, A11, A22, temp1);
    matrixAddition(newSize, B11, B22, temp2);
    strassen(newSize, temp1, temp2, M1);
 
    matrixAddition(newSize, A21, A22, temp1);
    strassen(newSize, temp1, B11, M2);
 
    matrixSubtraction(newSize, B12, B22, temp1);
    strassen(newSize, A11, temp1, M3);
 
    matrixSubtraction(newSize, B21, B11, temp1);
    strassen(newSize, A22, temp1, M4);
 
    matrixAddition(newSize, A11, A12, temp1);
    strassen(newSize, temp1, B22, M5);
 
    matrixSubtraction(newSize, A21, A11, temp1);
    matrixAddition(newSize, B11, B12, temp2);
    strassen(newSize, temp1, temp2, M6);
 
    matrixSubtraction(newSize, A12, A22, temp1);
    matrixAddition(newSize, B21, B22, temp2);
    strassen(newSize, temp1, temp2, M7);
 
    // Calculating C matrices
    matrixAddition(newSize, M1, M4, temp1);
    matrixSubtraction(newSize, temp1, M5, temp2);
    matrixAddition(newSize, temp2, M7, C11);
 
    matrixAddition(newSize, M3, M5, C12);
 
    matrixAddition(newSize, M2, M4, C21);
 
    matrixAddition(newSize, M1, M3, temp1);
    matrixSubtraction(newSize, temp1, M2, temp2);
    matrixAddition(newSize, temp2, M6, C22);
 
    // Combining C matrices into one
    for (int i = 0; i < newSize; i++) {
        for (int j = 0; j < newSize; j++) {
            C[i][j] = C11[i][j];
            C[i][j + newSize] = C12[i][j];
            C[i + newSize][j] = C21[i][j];
            C[i + newSize][j + newSize] = C22[i][j];
        }
    }
}
 
// Function to print a matrix
void printMatrix(int n, int matrix[][n]) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
}
 
int main() {
    int n;
    printf("Enter the size of matrices (power of 2): ");
    scanf("%d", &n);
 
    int A[n][n], B[n][n], C[n][n];
 
    printf("Enter elements of matrix A:\n");
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            scanf("%d", &A[i][j]);
 
    printf("Enter elements of matrix B:\n");
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            scanf("%d", &B[i][j]);
 
    strassen(n, A, B, C);
 
    printf("Resultant matrix C:\n");
    printMatrix(n, C);
 
    return 0;
}
