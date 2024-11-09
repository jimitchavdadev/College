#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_SYMBOLS 50
#define MAX_LITERALS 50

// Structure for Symbol Table
struct SymbolTable {
    char symbol[20];
    int address;
} symbolTable[MAX_SYMBOLS];

// Structure for Literal Table
struct LiteralTable {
    char literal[20];
    int address;
} literalTable[MAX_LITERALS];

int symbolCount = 0;
int literalCount = 0;
int lc = 0;  // Location Counter
int poolTable[10], poolCount = 0;

// Function to add symbol to symbol table
void addSymbol(char* symbol, int address) {
    if(symbol[0] == '=' || symbol[0] == '\0') return;
    
    for(int i = 0; i < symbolCount; i++) {
        if(strcmp(symbolTable[i].symbol, symbol) == 0) {
            return;
        }
    }
    
    strcpy(symbolTable[symbolCount].symbol, symbol);
    symbolTable[symbolCount].address = address;
    symbolCount++;
}

// Function to add literal to literal table
void addLiteral(char* literal) {
    for(int i = 0; i < literalCount; i++) {
        if(strcmp(literalTable[i].literal, literal) == 0) {
            return;
        }
    }
    
    strcpy(literalTable[literalCount].literal, literal);
    literalTable[literalCount].address = -1;
    literalCount++;
}

// Handle LTORG directive
void handleLTORG() {
    int start = (poolCount == 0) ? 0 : poolTable[poolCount - 1];
    for(int i = start; i < literalCount; i++) {
        literalTable[i].address = lc++;
    }
    poolTable[poolCount++] = literalCount;
}

// First Pass
void firstPass(char *input[], int size) {
    char line[100];
    char label[20], opcode[20], operand1[20], operand2[20];
    
    // Initialize pool table
    poolTable[poolCount++] = 0;
    
    for(int i = 0; i < size; i++) {
        strcpy(line, input[i]);
        label[0] = opcode[0] = operand1[0] = operand2[0] = '\0';
        
        // Parse the line
        char *token = strtok(strdup(line), " ,");
        int tokenCount = 0;
        
        while(token != NULL) {
            switch(tokenCount) {
                case 0: strcpy(label, token); break;
                case 1: strcpy(opcode, token); break;
                case 2: strcpy(operand1, token); break;
                case 3: strcpy(operand2, token); break;
            }
            token = strtok(NULL, " ,");
            tokenCount++;
        }
        
        // If only two tokens, shift everything
        if(tokenCount == 2) {
            strcpy(operand1, opcode);
            strcpy(opcode, label);
            label[0] = '\0';
        }
        
        // Handle START
        if(strcmp(label, "START") == 0 || strcmp(opcode, "START") == 0) {
            lc = atoi(operand1);
            continue;
        }
        
        // Handle END
        if(strcmp(label, "END") == 0 || strcmp(opcode, "END") == 0) {
            handleLTORG();
            break;
        }
        
        // Handle LTORG
        if(strcmp(label, "LTORG") == 0 || strcmp(opcode, "LTORG") == 0) {
            handleLTORG();
            continue;
        }
        
        // Handle DS instruction
        if(strcmp(opcode, "DS") == 0) {
            addSymbol(label, lc);
            lc++;
            continue;
        }
        
        // Handle symbols in label field
        if(label[0] != '\0' && strcmp(label, "START") != 0 && 
           strcmp(label, "END") != 0 && strcmp(label, "LTORG") != 0) {
            addSymbol(label, lc);
        }
        
        // Handle operands
        if(operand1[0] == '=') {
            addLiteral(operand1);
        } else if(operand1[0] != '\0') {
            addSymbol(operand1, lc);
        }
        
        if(operand2[0] == '=') {
            addLiteral(operand2);
        } else if(operand2[0] != '\0') {
            addSymbol(operand2, lc);
        }
        
        lc++;
    }
}

int main() {
    char *input[] = {
        "START 100",
        "READ N",
        "MOVER B, ='1'",
        "MOVEM B, TERM",
        "MUL B, TERM",
        "LTORG",
        "MOVER C, ='2'",
        "MOVE B, ='5'",
        "LTORG",
        "DS '1'",
        "TERM DS '1'",
        "END"
    };
    int size = sizeof(input)/sizeof(input[0]);
    
    firstPass(input, size);
    
    // Display Symbol Table
    printf("\nSymbol Table:\n");
    printf("Symbol\tAddress\n");
    for(int i = 0; i < symbolCount; i++) {
        printf("%s\t%d\n", symbolTable[i].symbol, symbolTable[i].address);
    }
    
    // Display Literal Table
    printf("\nLiteral Table:\n");
    printf("Literal\tAddress\n");
    for(int i = 0; i < literalCount; i++) {
        printf("%s\t%d\n", literalTable[i].literal, literalTable[i].address);
    }
    
    return 0;
}