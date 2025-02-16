#include <stdio.h>
#include <string.h>

#define MAX_LINE_LENGTH 1024

// Define keywords and operators

char *keywords[] = {
    "auto", "break", "case", "char", "const", "continue", "default", "do",
    "double", "else", "enum", "extern", "float", "for", "goto", "if", "int",
    "long", "register", "return", "short", "signed", "sizeof", "static",
    "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"};

int num_keywords = sizeof(keywords) / sizeof(keywords[0]);

char *operators[] = {
    "+", "-", "*", "/", "%", "++", "--", "=", ";"};

int num_operators = sizeof(operators) / sizeof(operators[0]);

// Function to check if a string is a keyword
int is_keyword(char *word)
{
    for (int i = 0; i < num_keywords; i++)
    {
        if (strcmp(word, keywords[i]) == 0)
        {
            return 1;
        }
    }
    return 0;
}

// Function to count operators in a line
int count_operators(char *line)
{
    int count = 0;
    for (int i = 0; i < num_operators; i++)
    {
        char *op = operators[i];
        char *pos = line;
        while ((pos = strstr(pos, op)) != NULL)
        {
            count++;
            pos += strlen(op);
        }
    }
    return count;
}

void count_elements(char *filename)
{
    FILE *file = fopen(filename, "r");
    if (file == NULL)
    {
        perror("Failed to open file");
        return;
    }

    int keyword_count = 0;
    int operator_count = 0;
    int other_count = 0;

    char line[MAX_LINE_LENGTH];
    while (fgets(line, sizeof(line), file))
    {
        char *token = strtok(line, " \t\n");
        while (token != NULL)
        {
            if (is_keyword(token))
            {
                keyword_count++;
            }
            else
            {
                operator_count += count_operators(token);
                // Assuming the remaining tokens are other elements
                if (!is_keyword(token))
                {
                    other_count++;
                }
            }
            token = strtok(NULL, " \t\n");
        }
        operator_count += count_operators(line);
    }

    fclose(file);

    FILE *output_file = fopen("output.txt", "a");
    if (output_file == NULL)
    {
        perror("Failed to open output file");
        return;
    }

    fprintf(output_file, "Keyword count: %d\n", keyword_count);
    fprintf(output_file, "Operator count: %d\n", operator_count);
    fprintf(output_file, "Other count: %d\n", other_count);

    fclose(output_file);
}

int main()
{
    // Replace "sample.c" with the path to your file
    count_elements("sample.c");
    return 0;
}
