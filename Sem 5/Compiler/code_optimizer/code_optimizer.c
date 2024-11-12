#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_EXPR 100
#define MAX_VAR_NAME 20
#define MAX_LINE_LENGTH 100

typedef struct
{
    char myExpr[MAX_LINE_LENGTH];
    char myVar[MAX_VAR_NAME]; // The result variable name
} MyExpression;

MyExpression myList[MAX_EXPR];
int count = 0;

// Function to find if an expression already exists
int findMyExpr(const char *expr)
{
    for (int i = 0; i < count; i++)
    {
        if (strcmp(myList[i].myExpr, expr) == 0)
        {
            return i; // Found it
        }
    }
    return -1; // Not found
}

// Function to add a new expression
void addMyExpr(const char *expr, const char *var)
{
    if (count < MAX_EXPR)
    {
        strncpy(myList[count].myExpr, expr, MAX_LINE_LENGTH - 1);
        myList[count].myExpr[MAX_LINE_LENGTH - 1] = '\0';
        strncpy(myList[count].myVar, var, MAX_VAR_NAME - 1);
        myList[count].myVar[MAX_VAR_NAME - 1] = '\0'; // Null terminate
        count++;                                      // Increment
    }
    else
    {
        printf("List full!\n");
    }
}

// Function to optimize the code
void optimizeCode(char code[][MAX_LINE_LENGTH], int size)
{
    for (int i = 0; i < size; i++)
    {
        char resVar[MAX_VAR_NAME], expr[MAX_LINE_LENGTH];
        // Checking if the format is correct: var = expression
        if (sscanf(code[i], "%s = %[^\n]", resVar, expr) == 2)
        {
            int foundIndex = findMyExpr(expr);
            if (foundIndex != -1)
            {
                // Found a match, reuse the existing variable
                snprintf(code[i], MAX_LINE_LENGTH, "%s = %s", resVar, myList[foundIndex].myVar);
            }
            else
            {
                // Add the new expression with the current variable name
                addMyExpr(expr, resVar);
            }
        }
    }
}

// Print the optimized code
void printMyCode(char code[][MAX_LINE_LENGTH], int size)
{
    printf("Optimized Code:\n");
    for (int i = 0; i < size; i++)
    {
        printf("%s\n", code[i]);
    }
}

int main()
{
    // Sample code
    char code[7][MAX_LINE_LENGTH] = {
        "a = x + y",
        "b = x + y",
        "c = a * z",
        "d = b * z",
        "e = a * z",
        "f = x + y",
        "g = b * z"};

    int size = sizeof(code) / sizeof(code[0]);

    optimizeCode(code, size);
    printMyCode(code, size);

    return 0;
}