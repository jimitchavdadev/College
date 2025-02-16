#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_MNEMONICS 29
#define MAX_LITERALS 10
#define MAX_SYMBOLS 10
#define MAX_POOLS 10
#define MAX_CODE_LINES 100

struct Mnemonic
{
    char mnemonic[10];
    char class[3];
    char machineCode[10];
    int length;
};

struct Literal
{
    char literal[10];
    int address;
};

struct Symbol
{
    char symbol[10];
    int address;
};

struct Pool
{
    int startIndex;
};

int findMnemonic(struct Mnemonic mnemonics[], char *mnemonic, int count)
{
    for (int i = 0; i < count; i++)
    {
        if (strcmp(mnemonics[i].mnemonic, mnemonic) == 0)
        {
            return i;
        }
    }
    return -1;
}

int findSymbol(struct Symbol symbols[], char *symbol, int symbolCount)
{
    for (int i = 0; i < symbolCount; i++)
    {
        if (strcmp(symbols[i].symbol, symbol) == 0)
        {
            return i;
        }
    }
    return -1;
}

int addSymbol(struct Symbol symbols[], char *symbol, int *symbolCount,
              int currentAddress)
{
    strcpy(symbols[*symbolCount].symbol, symbol);
    symbols[*symbolCount].address = currentAddress;
    (*symbolCount)++;
    return *symbolCount - 1;
}

int isValidSymbol(char *str) { return !isdigit(str[0]); }

void printIntermediateCode(FILE *outputFile, char ic[MAX_CODE_LINES][50],
                           char assemblyCode[MAX_CODE_LINES][50],
                           char machineCode[MAX_CODE_LINES][20],
                           int lc[MAX_CODE_LINES], int icCount)
{
    fprintf(outputFile, "\nSRC                 LC                 IC             "
                        "          Machine Code\n");
    fprintf(outputFile, ""
                        "\n");

    for (int i = 0; i < icCount; i++)
    {
        fprintf(outputFile, "%-18s %-9d %-20s %-30s\n", assemblyCode[i], lc[i],
                ic[i], machineCode[i]);
    }
}

void printLiteralTable(FILE *outputFile, struct Literal literals[],
                       int literalCount)
{
    fprintf(outputFile, "\nLiteral Table:\n");
    fprintf(outputFile, "%-10s %-10s %-10s\n", "Index", "Literal", "Address");
    for (int i = 0; i < literalCount; i++)
    {
        fprintf(outputFile, "%-10d %-10s %-10d\n", i, literals[i].literal,
                literals[i].address);
    }
}

void printSymbolTable(FILE *outputFile, struct Symbol symbols[],
                      int symbolCount)
{
    fprintf(outputFile, "\nSymbol Table:\n");
    fprintf(outputFile, "%-10s %-10s %-10s\n", "Index", "Symbol", "Address");
    for (int i = 0; i < symbolCount; i++)
    {
        fprintf(outputFile, "%-10d %-10s %-10d\n", i, symbols[i].symbol,
                symbols[i].address);
    }
}

void printPoolTable(FILE *outputFile, struct Pool pools[], int poolCount)
{
    fprintf(outputFile, "\nPool Table:\n");
    fprintf(outputFile, "%-15s %-20s\n", "Pool No.", "Literal Start Index");
    for (int i = 0; i < poolCount; i++)
    {
        fprintf(outputFile, "%-15d %-20d\n", i, pools[i].startIndex);
    }
}

int main()
{
    struct Mnemonic mnemonics[MAX_MNEMONICS] = {
        {"STOP", "IS", "00", 1}, {"ADD", "IS", "01", 1}, {"SUB", "IS", "02", 1}, {"MULTI", "IS", "03", 1}, {"MOVER", "IS", "04", 1}, {"MOVEM", "IS", "05", 1}, {"COMP", "IS", "06", 1}, {"BC", "IS", "07", 1}, {"DIV", "IS", "08", 1}, {"READ", "IS", "09", 1}, {"PRINT", "IS", "10", 1}, {"START", "AD", "01", 0}, {"END", "AD", "02", 0}, {"ORIGIN", "AD", "03", 0}, {"EQU", "AD", "04", 0}, {"LTORG", "AD", "05", 0}, {"DS", "DL", "01", 0}, {"DC", "DL", "02", 1}, {"AREG", "RG", "01", 0}, {"BREG", "RG", "02", 0}, {"CREG", "RG", "03", 0}, {"EQ", "CC", "03", 0}, {"LT", "CC", "01", 0}, {"GT", "CC", "04", 0}, {"LE", "CC", "02", 0}, {"GE", "CC", "05", 0}, {"NE", "CC", "06", 0}};

    struct Literal literals[MAX_LITERALS];
    struct Symbol symbols[MAX_SYMBOLS];
    struct Pool pools[MAX_POOLS];
    int literalCount = 0, symbolCount = 0, poolCount = 0, currentAddress = 0,
        icCount = 0;
    char intermediateCode[MAX_CODE_LINES][50];
    char assemblyCode[MAX_CODE_LINES][50];
    char machineCode[MAX_CODE_LINES][20];
    int lc[MAX_CODE_LINES];
    char line[100], mnemonic[10], operand1[10], operand2[10];

    FILE *file = fopen("program.asm", "r");
    FILE *outputFile = fopen("Output.txt", "w");

    if (file == NULL || outputFile == NULL)
    {
        printf("Error opening files!\n");
        return 1;
    }

    pools[poolCount++].startIndex = literalCount;

    while (fgets(line, sizeof(line), file))
    {
        strcpy(operand1, "");
        strcpy(operand2, "");

        sscanf(line, "%s %s %s", mnemonic, operand1, operand2);

        int mIndex = findMnemonic(mnemonics, mnemonic, MAX_MNEMONICS);
        if (mIndex != -1)
        {
            lc[icCount] = currentAddress;

            if (strcmp(mnemonics[mIndex].mnemonic, "START") == 0)
            {
                currentAddress = atoi(operand1);
                sprintf(assemblyCode[icCount], "%s %s", mnemonic, operand1);
                sprintf(intermediateCode[icCount], "(AD, %s) (C, %d)",
                        mnemonics[mIndex].machineCode, currentAddress);
                sprintf(machineCode[icCount++], "-");
            }
            else if (strcmp(mnemonics[mIndex].mnemonic, "ORIGIN") == 0)
            {
                currentAddress = atoi(operand1);
                sprintf(assemblyCode[icCount], "%s %s", mnemonic, operand1);
                sprintf(intermediateCode[icCount], "(AD, %s) (C, %d)",
                        mnemonics[mIndex].machineCode, currentAddress);
                sprintf(machineCode[icCount++], "-");
            }
            else if (strcmp(mnemonics[mIndex].mnemonic, "LTORG") == 0 ||
                     strcmp(mnemonics[mIndex].mnemonic, "END") == 0)
            {
                for (int i = pools[poolCount - 1].startIndex; i < literalCount; i++)
                {
                    literals[i].address = currentAddress++;
                }
                if (strcmp(mnemonics[mIndex].mnemonic, "LTORG") == 0)
                {
                    pools[poolCount++].startIndex = literalCount;
                }
                sprintf(assemblyCode[icCount], "%s", mnemonic);
                sprintf(intermediateCode[icCount], "(AD, %s)",
                        mnemonics[mIndex].machineCode);
                sprintf(machineCode[icCount++], "-");
            }
            else if (operand2[0] == '=')
            {
                strcpy(literals[literalCount].literal, operand2);
                sprintf(assemblyCode[icCount], "%s %s, %s", mnemonic, operand1,
                        operand2);
                sprintf(intermediateCode[icCount], "(IS, %s) (%s) (L, %d)",
                        mnemonics[mIndex].machineCode, operand1, literalCount);
                sprintf(machineCode[icCount++], "%s %s %d",
                        mnemonics[mIndex].machineCode, operand1, literalCount);
                literalCount++;
                currentAddress++;
            }
            else if (isValidSymbol(operand2))
            {
                int symbolIndex = findSymbol(symbols, operand2, symbolCount);
                if (symbolIndex == -1)
                {
                    symbolIndex =
                        addSymbol(symbols, operand2, &symbolCount, currentAddress);
                }
                sprintf(assemblyCode[icCount], "%s %s, %s", mnemonic, operand1,
                        operand2);
                sprintf(intermediateCode[icCount], "(IS, %s) (%s) (S, %d)",
                        mnemonics[mIndex].machineCode, operand1, symbolIndex);
                sprintf(machineCode[icCount++], "%s %s %d",
                        mnemonics[mIndex].machineCode, operand1, symbolIndex);
                currentAddress++;
            }
        }
    }

    printIntermediateCode(outputFile, intermediateCode, assemblyCode, machineCode,
                          lc, icCount);
    printSymbolTable(outputFile, symbols, symbolCount);
    printLiteralTable(outputFile, literals, literalCount);
    printPoolTable(outputFile, pools, poolCount);

    fclose(file);
    fclose(outputFile);

    return 0;
}