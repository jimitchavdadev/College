%{
#include <stdio.h>

int vowel_count = 0;
%}

%%

[aeiouAEIOU]    { vowel_count++; }

.                ;  /* Ignore all other characters */

%%

int main() {
    yylex();
    printf("Number of vowels: %d\n", vowel_count);
    return 0;
}
