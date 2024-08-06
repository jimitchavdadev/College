%{
#include<stdio.h>
int lines=0, words=0, characters=0;
%}
%%
\n { lines++; words++; characters++; }
[\t ' '] { words++; characters++; }
. { characters++; }
%%

main(void)
{
    yylex();
    printf("This file contains ...");
    printf("\n\t%d lines", lines);
    printf("\n\t%d words", words);
    printf("\n\t%d characters\n", characters);
}

int yywrap()
{
    return 1;
}
