%{
#include <stdio.h>
#include <string.h>

int token_count = 0;
%}

%%

[ \t\n]+                   ; // Ignore whitespace
[a-zA-Z_][a-zA-Z0-9_]*     { printf("Token: %s, Length: %d\n", yytext, strlen(yytext)); token_count++; }
[0-9]+                     { printf("Token: %s, Length: %d\n", yytext, strlen(yytext)); token_count++; }
.                          { printf("Token: %s, Length: %d\n", yytext, strlen(yytext)); token_count++; }

%%

int main()
{
    yylex();
    printf("Total number of tokens: %d\n", token_count);
    return 0;
}

int yywrap()
{
    return 1;
}
