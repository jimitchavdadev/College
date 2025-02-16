#include <stdio.h>
 #define MAX_SIZE 10 
void Multiply(int a[MAX_SIZE][MAX_SIZE], int b[MAX_SIZE][MAX_SIZE], int result[MAX_SIZE][MAX_SIZE], int r, int c) {
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            result[i][j] = 0;
            for (int k = 0; k < c; k++) { // Assuming square matrices for simplicity
                result[i][j] += a[i][k] * b[k][j];
            }
        }
    }
}
 void PrintMatrix(int matrix[MAX_SIZE][MAX_SIZE], int r, int c) {
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
}
 int main() {
    int r, c;
    int a[MAX_SIZE][MAX_SIZE], b[MAX_SIZE][MAX_SIZE], result[MAX_SIZE][MAX_SIZE];
     printf("Enter the number of rows and columns of matrix: ");
    scanf("%d%d", &r, &c);
    printf("Enter the elements of matrix A:\n");
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            scanf("%d", &a[i][j]);
        }
    }
     printf("Enter the elements of matrix B:\n");
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            scanf("%d", &b[i][j]);
        }
    }
 
    // No need to input matrix C, as it will be the result of A * B
    Multiply(a, b, result, r, c);
 
    printf("Resultant matrix C after multiplication:\n");
    PrintMatrix(result, r, c);
 
    return 0;
 }