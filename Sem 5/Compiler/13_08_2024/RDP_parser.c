#include <stdio.h>
#include <string.h>

#define parsed 1
#define notparsed 0
int Exp(), Expdash(), Term(), Termdash(), Factor();

const char *pointer;
char string[100];

int main()
{
    puts("Enter the string");
    scanf("%s", string);
    pointer = string;
    if (Exp() && *pointer == '\0')
    {
        printf("String parsed");
        return 0;
    }
    else
    {
        printf("String not parsed");
        return 1;
    }
}

int Exp()
{
    if (Term())
    {
        if (Expdash())
            return parsed;
        else
            return notparsed;
    }
    else
        return notparsed;
}

int Expdash()
{
    if (*pointer == '+')
    {
        pointer++;
        if (Term())
        {
            if (Expdash())
                return parsed;
            else
                return notparsed;
        }
        else
            return notparsed;
    }
    else
    {
        return parsed;
    }
}

int Term()
{
    if (Factor())
    {
        if (Termdash())
            return parsed;
        else
            return notparsed;
    }
    else
        return notparsed;
}

int Termdash()
{
    if (*pointer == '*')
    {
        pointer++;
        if (Factor())
        {
            if (Termdash())
                return parsed;
            else
                return notparsed;
        }
        else
            return notparsed;
    }
    else
    {
        return parsed;
    }
}

int Factor()
{
    if (*pointer == '(')
    {
        pointer++;
        if (Exp())
        {
            if (*pointer == ')')
            {
                pointer++;
                return parsed;
            }
            else
                return notparsed;
        }
        else
            return notparsed;
    }
    else if (strncmp(pointer, "id", 2) == 0)
    {
        pointer += 2;
        return parsed;
    }
    else
        return notparsed;
}