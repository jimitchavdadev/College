%{
#include <stdio.h>
%}

%%

[ \t]+            { fprintf(yyout, " "); }  // Replace multiple spaces and tabs with a single space
\n                 { fprintf(yyout, "\n"); }  // Keep newlines but replace multiple newlines with a single newline
.                  { fprintf(yyout, "%s", yytext); }  // Copy other characters as-is

%%

int main()
{
    extern FILE *yyin, *yyout;

    yyin = fopen("sample.txt", "r");
    if (!yyin) {
        perror("fopen");
        return 1;
    }

    yyout = fopen("Output.txt", "w");
    if (!yyout) {
        perror("fopen");
        fclose(yyin);
        return 1;
    }

    yylex();

    fclose(yyin);
    fclose(yyout);

    return 0;
}

int yywrap()
{
    return 1;
}
