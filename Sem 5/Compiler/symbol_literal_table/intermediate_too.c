#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_SYMBOLS 100
#define MAX_LITERALS 100
#define MAX_CODE_LINES 200

typedef struct {
    char label[20];
    int address;
} Symbol;

typedef struct {
    char literal[20];
    int address;
} Literal;

Symbol symbolTable[MAX_SYMBOLS];
Literal literalTable[MAX_LITERALS];
int symbolCount = 0;
int literalCount = 0;

void addSymbol(char *label, int address) {
    strcpy(symbolTable[symbolCount].label, label);
    symbolTable[symbolCount].address = address;
    symbolCount++;
}

void addLiteral(char *literal, int address) {
    strcpy(literalTable[literalCount].literal, literal);
    literalTable[literalCount].address = address;
    literalCount++;
}

void printSymbolTable() {
    printf("\nSymbol Table:\n");
    printf("Label\tAddress\n");
    for (int i = 0; i < symbolCount; i++) {
        printf("%s\t%d\n", symbolTable[i].label, symbolTable[i].address);
    }
}

void printLiteralTable() {
    printf("\nLiteral Table:\n");
    printf("Literal\tAddress\n");
    for (int i = 0; i < literalCount; i++) {
        printf("%s\t%d\n", literalTable[i].literal, literalTable[i].address);
    }
}

void generateThreeAddressCode(char code[][50], int n) {
    FILE *file = fopen("tac.txt", "w");
    if (!file) {
        printf("Error: Could not create three-address code file.\n");
        return;
    }

    int tempVarCount = 0;

    fprintf(file, "Three Address Code (TAC):\n");

    for (int i = 0; i < n; i++) {
        char label[20] = "-", opcode[10] = "-", operand1[20] = "-", operand2[20] = "-";
        
        // Parse the instruction line
        sscanf(code[i], "%s %s %s %s", label, opcode, operand1, operand2);

        // Add label to the symbol table if it exists
        if (strcmp(label, "-") != 0) {
            addSymbol(label, i * 4); // Address is a placeholder here
        }

        // Check and add literals regardless of instruction type
        if (operand1[0] == '=') {
            addLiteral(operand1, i * 4);
        }
        if (operand2[0] == '=') {
            addLiteral(operand2, i * 4 + 1);
        }

        // Generate TAC based on the opcode
        if (strcmp(opcode, "MOV") == 0) {
            fprintf(file, "%s = %s\n", operand1, operand2);
        } else if (strcmp(opcode, "ADD") == 0) {
            fprintf(file, "t%d = %s + %s\n", tempVarCount, operand1, operand2);
            fprintf(file, "%s = t%d\n", operand1, tempVarCount);
            tempVarCount++;
        } else if (strcmp(opcode, "SUB") == 0) {
            fprintf(file, "t%d = %s - %s\n", tempVarCount, operand1, operand2);
            fprintf(file, "%s = t%d\n", operand1, tempVarCount);
            tempVarCount++;
        } else if (strcmp(opcode, "MUL") == 0) {
            fprintf(file, "t%d = %s * %s\n", tempVarCount, operand1, operand2);
            fprintf(file, "%s = t%d\n", operand1, tempVarCount);
            tempVarCount++;
        } else if (strcmp(opcode, "DIV") == 0) {
            fprintf(file, "t%d = %s / %s\n", tempVarCount, operand1, operand2);
            fprintf(file, "%s = t%d\n", operand1, tempVarCount);
            tempVarCount++;
        } else if (strcmp(opcode, "DATA") == 0) {
            fprintf(file, "%s = %s\n", label, operand1);
        } else if (strcmp(opcode, "JMP") == 0) {
            fprintf(file, "goto %s\n", operand1);
        } else if (strcmp(opcode, "STOP") == 0) {
            fprintf(file, "halt\n");
        }
    }

    fclose(file);
    printf("Three-address code has been saved to 'tac.txt'.\n");
}

int main() {
    char code[MAX_CODE_LINES][50];
    int n = 0;

    // Open input file
    FILE *inputFile = fopen("input.txt", "r");
    if (!inputFile) {
        printf("Error: Could not open input file 'input.txt'.\n");
        return 1;
    }

    // Read lines from file
    while (fgets(code[n], sizeof(code[n]), inputFile) != NULL) {
        code[n][strcspn(code[n], "\n")] = '\0';  // Remove newline
        n++;
    }
    fclose(inputFile);

    // Generate three-address code and print tables
    generateThreeAddressCode(code, n);
    printSymbolTable();
    printLiteralTable();

    return 0;
}
