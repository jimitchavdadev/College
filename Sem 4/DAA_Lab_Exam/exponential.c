// C program to calculate pow(x,n)
#include <stdio.h>

/* Function to calculate x raised to the power y */
int power(int x, unsigned int y)
{
    if (y == 0)
        return 1;
    else if (y % 2 == 0)
        return power(x, y / 2) * power(x, y / 2);
    else
        return x * power(x, y / 2) * power(x, y / 2);
}

/* Driver code */
int main()
{
    int x = 2;
    unsigned int y = 3;

    // Function call
    printf("%d", power(x, y));
    return 0;
}
