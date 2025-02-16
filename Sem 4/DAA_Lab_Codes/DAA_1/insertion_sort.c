#include <stdio.h>

void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int currentElement = arr[i];
        int j = i - 1;

        while (j >= 0 && currentElement < arr[j]) {
            arr[j + 1] = arr[j];
            j--;
        }

        arr[j + 1] = currentElement;
    }
}

int main() {
    int myArray[] = {12, 11, 13, 5, 6};

    int size = sizeof(myArray) / sizeof(myArray[0]);

    insertionSort(myArray, size);

    printf("Sorted array: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", myArray[i]);
    }
    printf("\n");
    return 0;
}
