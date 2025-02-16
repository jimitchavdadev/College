%{
#include <stdio.h>
%}

%%
"SELECT"([^;]*";") { printf("SELECT statement: %s\n", yytext); }
"INSERT"([^;]*";") { printf("INSERT statement: %s\n", yytext); }
"UPDATE"([^;]*";") { printf("UPDATE statement: %s\n", yytext); }
"DELETE"([^;]*";") { printf("DELETE statement: %s\n", yytext); }
"CREATE"([^;]*";") { printf("CREATE statement: %s\n", yytext); }
"DROP"([^;]*";")   { printf("DROP statement: %s\n", yytext); }
.                  { /* Ignore other characters */ }
%%

int main(void)
{
    yyin = fopen("input.sql", "r");
    if (!yyin) {
        perror("fopen");
        return 1;
    }
    yylex();
    fclose(yyin);
    return 0;
}

int yywrap()
{
    return 1;
}
