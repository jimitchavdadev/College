#include <stdio.h>
#include <string.h>

#define MAX_EXPR 100
#define MAX_LEN 100
#define MAX_TAC 100

// Structure to hold an expression
typedef struct
{
    char variable[10];
    char expression[MAX_LEN];
} Expr;

// Structure for three-address code (TAC)
typedef struct
{
    char result[10];
    char arg1[10];
    char op[3];
    char arg2[10];
} TAC;

TAC tac[MAX_TAC];
int tac_count = 0;

// Function to eliminate common subexpressions
void eliminateCommonSubExpr(Expr *expressions, int size)
{
    for (int i = 0; i < size; i++)
    {
        for (int j = i + 1; j < size; j++)
        {
            if (strstr(expressions[j].expression, expressions[i].expression))
            {
                printf("Common subexpression found: %s in expression %s\n", expressions[i].expression, expressions[j].expression);

                char tempExpr[MAX_LEN];
                strcpy(tempExpr, expressions[j].expression);
                char *pos = strstr(tempExpr, expressions[i].expression);
                if (pos != NULL)
                {
                    int len = pos - tempExpr;
                    char newExpr[MAX_LEN] = {0};
                    strncpy(newExpr, tempExpr, len);
                    strcat(newExpr, expressions[i].variable);
                    strcat(newExpr, pos + strlen(expressions[i].expression));
                    strcpy(expressions[j].expression, newExpr);
                    printf("Optimized expression: %s = %s\n", expressions[j].variable, expressions[j].expression);
                }
            }
        }
    }
}

// Convert expression to Three-Address Code
void convertToTAC(Expr *expressions, int size)
{
    for (int i = 0; i < size; i++)
    {
        char *expr = expressions[i].expression;
        char *var = expressions[i].variable;
        char temp[MAX_LEN];
        int temp_count = 1;

        // Split the expression by tokens (i.e., by operators +, -, *, /)
        char *token = strtok(expr, "+-*/"); // Change 'char' to 'char*'
        strcpy(temp, token);                // Copy the string token

        // Generate temporary variable for the first token
        char tempVar[10];
        sprintf(tempVar, "t%d", temp_count++);
        strcpy(tac[tac_count].result, tempVar);
        strcpy(tac[tac_count].arg1, temp);
        strcpy(tac[tac_count].op, "=");
        tac[tac_count++].arg2[0] = '\0';

        // Continue processing the rest of the tokens
        while ((token = strtok(NULL, "+-*/")) != NULL)
        { // Same here, 'char*'
            // Generate temporary variables for each operation
            sprintf(tempVar, "t%d", temp_count++);
            strcpy(tac[tac_count].result, tempVar);
            strcpy(tac[tac_count].arg1, temp);  // Use the previous temporary variable
            strcpy(tac[tac_count].op, "+");     // Replace "+" with other operators if needed
            strcpy(tac[tac_count].arg2, token); // Copy the next token string
            strcpy(temp, tempVar);              // Update the temporary variable for the next iteration
            tac_count++;
        }

        // Assign the final result to the target variable
        strcpy(tac[tac_count].result, var);
        strcpy(tac[tac_count].arg1, temp);
        strcpy(tac[tac_count].op, "=");
        tac[tac_count++].arg2[0] = '\0';
    }
}

// Function to print TAC
void printTAC()
{
    printf("\nThree-Address Code (TAC):\n");
    for (int i = 0; i < tac_count; i++)
    {
        if (tac[i].arg2[0] == '\0')
            printf("%s = %s\n", tac[i].result, tac[i].arg1);
        else
            printf("%s = %s %s %s\n", tac[i].result, tac[i].arg1, tac[i].op, tac[i].arg2);
    }
}

// Function to print Quadruple table
void printQuadruple()
{
    printf("\nQuadruple Representation:\n");
    printf("Op    Arg1   Arg2   Result\n");
    for (int i = 0; i < tac_count; i++)
    {
        printf("%-5s %-6s %-6s %-6s\n", tac[i].op, tac[i].arg1, tac[i].arg2, tac[i].result);
    }
}

// Function to print Triple table
void printTriple()
{
    printf("\nTriple Representation:\n");
    printf("Index  Op    Arg1   Arg2\n");
    for (int i = 0; i < tac_count; i++)
    {
        printf("%-6d %-5s %-6s %-6s\n", i, tac[i].op, tac[i].arg1, tac[i].arg2);
    }
}

// Function to print Indirect Triple table
void printIndirectTriple()
{
    printf("\nIndirect Triple Representation:\n");
    printf("Index  Triple Index\n");
    for (int i = 0; i < tac_count; i++)
    {
        printf("%-6d %-6d\n", i, i);
    }
}

int main()
{
    int size;

    // Input the number of expressions
    printf("Enter the number of expressions: ");
    scanf("%d", &size);

    // Array to store expressions
    Expr expressions[MAX_EXPR];

    // Input expressions from the user
    printf("Enter %d expressions in the form variable=expression (e.g., z=a+b):\n", size);
    for (int i = 0; i < size; i++)
    {
        printf("Expression %d: ", i + 1);
        scanf(" %[^=]=%[^\n]%*c", expressions[i].variable, expressions[i].expression); // Read variable and expression
    }

    // Show original expressions
    printf("\nOriginal expressions:\n");
    for (int i = 0; i < size; i++)
    {
        printf("%s = %s\n", expressions[i].variable, expressions[i].expression);
    }

    // Eliminate common subexpressions
    eliminateCommonSubExpr(expressions, size);

    // Convert expressions to TAC
    convertToTAC(expressions, size);

    // Print the Three-Address Code (TAC)
    printTAC();

    // Print Quadruple, Triple, and Indirect Triple representations
    printQuadruple();
    printTriple();
    printIndirectTriple();

    return 0;
}
