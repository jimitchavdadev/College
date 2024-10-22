%option yylineno

%{
  #include "y.tab.h"
  extern int yylval;
%}

NUMBER        ([0-9]+(".")?([0-9])*)
IDENTIFIER    ([a-zA-z_][a-zA-z_0-9]*)

%%

[\t ];

for             {return FOR;}
{NUMBER}        {return NUM;}
{IDENTIFIER}    {return ID;}
"<="            {return LE;}
">="            {return GE;}
"=="            {return EQ;}
"!="            {return NE;}
"||"            {return OR;}
"&&"            {return AND;}

.               {return yytext[0];}

\n              {yylval = yylineno;}

\n\n            {return 0;}

%%

int yywrap(void) {
    return 1;
}