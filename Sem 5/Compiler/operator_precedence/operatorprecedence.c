#include <stdio.h>
#include <string.h>

// Define constants for maximum stack size and number of operators
#define MAX_STACK_SIZE 100
#define NUM_OPERATORS 4

// List of operators used in the expression and the end marker '$'
const char *operators[NUM_OPERATORS] = {"id", "+", "*", "$"};

// Operator precedence table
char precedence_table[NUM_OPERATORS][NUM_OPERATORS] = {
    // id   +    *    $
    {' ', '>', '>', '>'}, // id
    {'<', '>', '<', '>'}, // +
    {'<', '>', '>', '>'}, // *
    {'<', '<', '<', ' '}  // $
};

// Function to find the index of an operator in the precedence table
int findOperatorIndex(const char *op)
{
    for (int i = 0; i < NUM_OPERATORS; i++)
    {
        if (strcmp(operators[i], op) == 0)
        {
            return i;
        }
    }
    return -1;
}

int main()
{
    char stack[MAX_STACK_SIZE][10]; // Stack to store symbols during parsing
    int top = 0;                    // Stack pointer, initialized to the bottom of the stack

    // Initialize the stack with the end marker '$'
    strcpy(stack[top], "$");

    char input[MAX_STACK_SIZE];
    // Prompt the user to input a string representing an arithmetic expression
    printf("Enter the input string (e.g., id+id*id$): ");
    fgets(input, MAX_STACK_SIZE, stdin); // Read input from the user
    input[strcspn(input, "\n")] = '\0';  // Remove the newline character

    const char *currentInput = input;

    // Process each symbol in the input string
    while (*currentInput != '\0')
    {
        char topOfStack[10]; // Top symbol of the stack
        strcpy(topOfStack, stack[top]);

        char currentSymbol[10];
        if (strncmp(currentInput, "id", 2) == 0) // Handle "id" as a multi-character symbol
        {
            strcpy(currentSymbol, "id");
            currentInput += 2; // Move input pointer past "id"
        }
        else
        {
            snprintf(currentSymbol, sizeof(currentSymbol), "%c", *currentInput);
            currentInput++;
        }

        int topIndex = findOperatorIndex(topOfStack);
        int currentIndex = findOperatorIndex(currentSymbol);

        char precedence = precedence_table[topIndex][currentIndex];

        if (precedence == '<' || precedence == ' ') // Push the current symbol onto the stack
        {
            top++;
            strcpy(stack[top], currentSymbol);
        }
        else if (precedence == '>') // Pop the stack until precedence is no longer greater
        {
            while (top > 0 && precedence_table[findOperatorIndex(stack[top])][currentIndex] == '>')
            {
                top--; // Move the stack pointer down
            }
            top++;
            strcpy(stack[top], currentSymbol);
        }
        else
        {
            printf("Error: Invalid precedence relation\n");
            return 0;
        }
    }

    // Pop remaining items from the stack
    while (top > 0)
    {
        top--;
    }

    // Check if parsing was successful by ensuring only the '$' symbol remains in the stack
    if (top == 0 && strcmp(stack[top], "$") == 0)
    {
        printf("Parsing completed successfully\n");
        return 1;
    }
    else
    {
        printf("Parsing failed\n");
        return 0;
    }
}
