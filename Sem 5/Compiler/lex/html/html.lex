%{
#include <stdio.h>
%}

%%
"<"[^>]*">"  { printf("%s\n", yytext); }
.            { /* Ignore other characters */ }
%%

int main(void)
{
    yyin = fopen("input.html", "r");
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
