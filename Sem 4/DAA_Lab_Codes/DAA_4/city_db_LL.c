#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// Structure to hold city information
typedef struct
{
    char name[100];
    int x;
    int y;
} City;

// Node structure for the unordered list
typedef struct Node
{
    City city;
    struct Node *next;
} Node;

// Function prototypes
Node *insertRecord(Node *head, City city);
Node *deleteRecord(Node *head, const char *name);
Node *deleteRecordByCoordinates(Node *head, int x, int y);
void searchRecordByName(Node *head, const char *name);
void searchRecordByCoordinates(Node *head, int x, int y);
void printRecordsWithinDistance(Node *head, int x, int y, double distance);
double calculateDistance(int x1, int y1, int x2, int y2);

int main()
{
    Node *head = NULL;
    char choice;
    City city;
    char cityName[100];
    int cityX, cityY;
    double distance;

    do
    {
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

        switch (choice)
        {
        case '1':
            printf("Enter city name: ");
            scanf("%s", city.name);
            printf("Enter city coordinates (x y): ");
            scanf("%d %d", &city.x, &city.y);
            head = insertRecord(head, city);
            break;
        case '2':
            printf("Enter city name to delete: ");
            scanf("%s", cityName);
            head = deleteRecord(head, cityName);
            break;
        case '3':
            printf("Enter city coordinates (x y) to delete: ");
            scanf("%d %d", &cityX, &cityY);
            head = deleteRecordByCoordinates(head, cityX, cityY);
            break;
        case '4':
            printf("Enter city name to search: ");
            scanf("%s", cityName);
            searchRecordByName(head, cityName);
            break;
        case '5':
            printf("Enter city coordinates (x y) to search: ");
            scanf("%d %d", &cityX, &cityY);
            searchRecordByCoordinates(head, cityX, cityY);
            break;
        case '6':
            printf("Enter point coordinates (x y): ");
            scanf("%d %d", &cityX, &cityY);
            printf("Enter maximum distance: ");
            scanf("%lf", &distance);
            printRecordsWithinDistance(head, cityX, cityY, distance);
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
Node *insertRecord(Node *head, City city)
{
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->city = city;
    newNode->next = head;
    return newNode;
}

// Function to delete a record by name
Node *deleteRecord(Node *head, const char *name)
{
    Node *current = head;
    Node *prev = NULL;

    while (current != NULL)
    {
        if (strcmp(current->city.name, name) == 0)
        {
            if (prev == NULL)
            {
                head = current->next;
            }
            else
            {
                prev->next = current->next;
            }
            free(current);
            printf("Record with name '%s' deleted.\n", name);
            return head;
        }
        prev = current;
        current = current->next;
    }

    printf("Record with name '%s' not found.\n", name);
    return head;
}

// Function to delete a record by coordinates
Node *deleteRecordByCoordinates(Node *head, int x, int y)
{
    Node *current = head;
    Node *prev = NULL;

    while (current != NULL)
    {
        if (current->city.x == x && current->city.y == y)
        {
            if (prev == NULL)
            {
                head = current->next;
            }
            else
            {
                prev->next = current->next;
            }
            free(current);
            printf("Record at coordinates (%d, %d) deleted.\n", x, y);
            return head;
        }
        prev = current;
        current = current->next;
    }

    printf("Record at coordinates (%d, %d) not found.\n", x, y);
    return head;
}

// Function to search for a record by name
void searchRecordByName(Node *head, const char *name)
{
    Node *current = head;
    while (current != NULL)
    {
        if (strcmp(current->city.name, name) == 0)
        {
            printf("City found: %s (%d, %d)\n", current->city.name, current->city.x, current->city.y);
            return;
        }
        current = current->next;
    }
    printf("City with name '%s' not found.\n", name);
}

// Function to search for a record by coordinates
void searchRecordByCoordinates(Node *head, int x, int y)
{
    Node *current = head;
    while (current != NULL)
    {
        if (current->city.x == x && current->city.y == y)
        {
            printf("City found: %s (%d, %d)\n", current->city.name, current->city.x, current->city.y);
            return;
        }
        current = current->next;
    }
    printf("City at coordinates (%d, %d) not found.\n", x, y);
}

// Function to print all records within a given distance of a specified point
void printRecordsWithinDistance(Node *head, int x, int y, double distance)
{
    Node *current = head;
    while (current != NULL)
    {
        double dist = calculateDistance(x, y, current->city.x, current->city.y);
        if (dist <= distance)
        {
            printf("City within %f units: %s (%d, %d)\n", distance, current->city.name, current->city.x, current->city.y);
        }
        current = current->next;
    }
}

// Function to calculate distance between two points
double calculateDistance(int x1, int y1, int x2, int y2)
{
    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
}