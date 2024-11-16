%{
#include <stdio.h>
#include <string.h>

int keywords_count = 0;
int identifiers_count = 0;
int numbers_count = 0;
int others_count = 0;

void check_keyword(char* token);
%}

%%

"int"|"return"|"if"|"else"|"while"|"for" { check_keyword(yytext); }
[a-zA-Z_][a-zA-Z0-9_]*                   { printf("Identifier: %s\n", yytext); identifiers_count++; }
[0-9]+                                   { printf("Number: %s\n", yytext); numbers_count++; }
.                                        { printf("Other: %s\n", yytext); others_count++; }

%%

void check_keyword(char* token)
{
    printf("Keyword: %s\n", token);
    keywords_count++;
}

int main()
{
    yylex();
    printf("\nSummary:\n");
    printf("Identifiers: %d\n", identifiers_count);
    printf("Numbers: %d\n", numbers_count);
    printf("Others: %d\n", others_count);
    return 0;
}

int yywrap()
{
    return 1;
}
