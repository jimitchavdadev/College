#include <stdio.h>
#include <stdlib.h>

#define ROW_1 4
#define COL_1 4

#define ROW_2 4
#define COL_2 4

void print(char* display, int** matrix, int start_row, int start_column, int end_row, int end_column) {
    printf("\n%s =>\n", display);
    for (int i = start_row; i <= end_row; i++) {
        for (int j = start_column; j <= end_column; j++) {
            printf("%10d", matrix[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

void add_matrix(int** matrix_A, int** matrix_B, int** matrix_C, int split_index) {
    for (int i = 0; i < split_index; i++) {
        for (int j = 0; j < split_index; j++) {
            matrix_C[i][j] = matrix_A[i][j] + matrix_B[i][j];
        }
    }
}

int** multiply_matrix(int** matrix_A, int** matrix_B, int row_1, int col_1, int row_2, int col_2) {
    if (col_1 != row_2) {
        printf("\nError: The number of columns in Matrix A must be equal to the number of rows in Matrix B\n");
        return NULL;
    }

    int** result_matrix = (int**)malloc(row_1 * sizeof(int*));
    for (int i = 0; i < row_1; i++) {
        result_matrix[i] = (int*)malloc(col_2 * sizeof(int));
    }

    if (col_1 == 1) {
        result_matrix[0][0] = matrix_A[0][0] * matrix_B[0][0];
    } else {
        int split_index = col_1 / 2;

        int** result_matrix_00 = multiply_matrix(matrix_A, matrix_B, split_index, split_index, split_index, split_index);
        int** result_matrix_01 = multiply_matrix(matrix_A, matrix_B, split_index, col_1 - split_index, split_index, split_index);
        int** result_matrix_10 = multiply_matrix(matrix_A, matrix_B, row_1 - split_index, split_index, split_index, split_index);
        int** result_matrix_11 = multiply_matrix(matrix_A, matrix_B, row_1 - split_index, col_1 - split_index, split_index, split_index);

        add_matrix(result_matrix_00, result_matrix_01, result_matrix, split_index);
        add_matrix(result_matrix_10, result_matrix_11, result_matrix, split_index);

        for (int i = 0; i < split_index; i++) {
            free(result_matrix_00[i]);
            free(result_matrix_01[i]);
            free(result_matrix_10[i]);
            free(result_matrix_11[i]);
        }
        free(result_matrix_00);
        free(result_matrix_01);
        free(result_matrix_10);
        free(result_matrix_11);
    }
    return result_matrix;
}

int main() {
    int** matrix_A = (int**)malloc(ROW_1 * sizeof(int*));
    for (int i = 0; i < ROW_1; i++) {
        matrix_A[i] = (int*)malloc(COL_1 * sizeof(int));
        for (int j = 0; j < COL_1; j++) {
            matrix_A[i][j] = i + j + 1;
        }
    }

    print("Array A", matrix_A, 0, 0, ROW_1 - 1, COL_1 - 1);

    int** matrix_B = (int**)malloc(ROW_2 * sizeof(int*));
    for (int i = 0; i < ROW_2; i++) {
        matrix_B[i] = (int*)malloc(COL_2 * sizeof(int));
        for (int j = 0; j < COL_2; j++) {
            matrix_B[i][j] = i + j + 1;
        }
    }

    print("Array B", matrix_B, 0, 0, ROW_2 - 1, COL_2 - 1);

    int** result_matrix = multiply_matrix(matrix_A, matrix_B, ROW_1, COL_1, ROW_2, COL_2);

    if (result_matrix != NULL) {
        print("Result Array", result_matrix, 0, 0, ROW_1 - 1, COL_2 - 1);

        for (int i = 0; i < ROW_1; i++) {
            free(matrix_A[i]);
        }
        for (int i = 0; i < ROW_2; i++) {
            free(matrix_B[i]);
        }
        for (int i = 0; i < ROW_1; i++) {
            free(result_matrix[i]);
        }
        free(matrix_A);
        free(matrix_B);
        free(result_matrix);
    }

    return 0;
}
