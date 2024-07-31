#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_CITIES 100

// Structure to hold city information
typedef struct {
    char name[100];
    int x;
    int y;
} City;

// Function prototypes
int insertRecord(City cities[], int size, City city);
int deleteRecordByName(City cities[], int size, const char* name);
int deleteRecordByCoordinates(City cities[], int size, int x, int y);
void searchRecordByName(City cities[], int size, const char* name);
void searchRecordByCoordinates(City cities[], int size, int x, int y);
void printRecordsWithinDistance(City cities[], int size, int x, int y, double distance);
double calculateDistance(int x1, int y1, int x2, int y2);

int main() {
    City cities[MAX_CITIES];
    int size = 0;
    char choice;
    City city;
    char cityName[100];
    int cityX, cityY;
    double distance;

    do {
        printf("\nMenu:\n");
        printf("1. Insert a record\n");
        printf("2. Delete a record by name\n");
        printf("3. Delete a record by coordinates\n");
        printf("4. Search a record by name\n");
        printf("5. Search a record by coordinates\n");
        printf("6. Print records within a given distance of a specified point\n");
        printf("7. Exit\n");
        printf("Enter your choice: ");
        scanf(" %c", &choice);

        switch(choice) {
            case '1':
                printf("Enter city name: ");
                scanf("%s", city.name);
                printf("Enter city coordinates (x y): ");
                scanf("%d %d", &city.x, &city.y);
                size = insertRecord(cities, size, city);
                break;
            case '2':
                printf("Enter city name to delete: ");
                scanf("%s", cityName);
                size = deleteRecordByName(cities, size, cityName);
                break;
            case '3':
                printf("Enter city coordinates (x y) to delete: ");
                scanf("%d %d", &cityX, &cityY);
                size = deleteRecordByCoordinates(cities, size, cityX, cityY);
                break;
            case '4':
                printf("Enter city name to search: ");
                scanf("%s", cityName);
                searchRecordByName(cities, size, cityName);
                break;
            case '5':
                printf("Enter city coordinates (x y) to search: ");
                scanf("%d %d", &cityX, &cityY);
                searchRecordByCoordinates(cities, size, cityX, cityY);
                break;
            case '6':
                printf("Enter point coordinates (x y): ");
                scanf("%d %d", &cityX, &cityY);
                printf("Enter maximum distance: ");
                scanf("%lf", &distance);
                printRecordsWithinDistance(cities, size, cityX, cityY, distance);
                break;
            case '7':
                printf("Exiting program.\n");
                break;
            default:
                printf("Invalid choice. Please enter a number from 1 to 7.\n");
        }
    } while (choice != '7');

    return 0;
}

// Function to insert a record into the database
int insertRecord(City cities[], int size, City city) {
    if (size < MAX_CITIES) {
        cities[size++] = city;
        printf("Record inserted.\n");
    } else {
        printf("Database full. Cannot insert record.\n");
    }
    return size;
}

// Function to delete a record by name
int deleteRecordByName(City cities[], int size, const char* name) {
    for (int i = 0; i < size; i++) {
        if (strcmp(cities[i].name, name) == 0) {
            for (int j = i; j < size - 1; j++) {
                cities[j] = cities[j + 1];
            }
            printf("Record with name '%s' deleted.\n", name);
            return size - 1;
        }
    }
    printf("Record with name '%s' not found.\n", name);
    return size;
}

// Function to delete a record by coordinates
int deleteRecordByCoordinates(City cities[], int size, int x, int y) {
    for (int i = 0; i < size; i++) {
        if (cities[i].x == x && cities[i].y == y) {
            for (int j = i; j < size - 1; j++) {
                cities[j] = cities[j + 1];
            }
            printf("Record at coordinates (%d, %d) deleted.\n", x, y);
            return size - 1;
        }
    }
    printf("Record at coordinates (%d, %d) not found.\n", x, y);
    return size;
}

// Function to search for a record by name
void searchRecordByName(City cities[], int size, const char* name) {
    for (int i = 0; i < size; i++) {
        if (strcmp(cities[i].name, name) == 0) {
            printf("City found: %s (%d, %d)\n", cities[i].name, cities[i].x, cities[i].y);
            return;
        }
    }
    printf("City with name '%s' not found.\n", name);
}

// Function to search for a record by coordinates
void searchRecordByCoordinates(City cities[], int size, int x, int y) {
    for (int i = 0; i < size; i++) {
        if (cities[i].x == x && cities[i].y == y) {
            printf("City found: %s (%d, %d)\n", cities[i].name, cities[i].x, cities[i].y);
            return;
        }
    }
    printf("City at coordinates (%d, %d) not found.\n", x, y);
}

// Function to print all records within a given distance of a specified point
void printRecordsWithinDistance(City cities[], int size, int x, int y, double distance) {
    for (int i = 0; i < size; i++) {
        double dist = calculateDistance(x, y, cities[i].x, cities[i].y);
        if (dist <= distance) {
            printf("City within %f units: %s (%d, %d)\n", distance, cities[i].name, cities[i].x, cities[i].y);
        }
    }
}

// Function to calculate distance between two points
double calculateDistance(int x1, int y1, int x2, int y2) {
    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
}