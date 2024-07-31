#include <stdio.h>

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int arr[], int low, int high)
{
    int pivot = arr[high];
    int i = low - 1; 

    for (int j = low; j <= high - 1; j++)
    {
        if (arr[j] < pivot)
        {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }

    swap(&arr[i + 1], &arr[high]);
    return i + 1;
}

void quickSort(int arr[], int low, int high)
{
    if (low < high)
    {
        int pivotIndex = partition(arr, low, high);

        quickSort(arr, low, pivotIndex - 1);
        quickSort(arr, pivotIndex + 1, high);
    }
}

int main()
{
    int myArray[] = {64, 25, 12, 22, 11};

    int size = sizeof(myArray) / sizeof(myArray[0]);

    quickSort(myArray, 0, size - 1);

    printf("Sorted array: ");
    for (int i = 0; i < size; i++)
    {
        printf("%d ", myArray[i]);
    }
    printf("\n");
    return 0;
}
