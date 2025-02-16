#include <stdio.h>
#include <string.h>

// Helper function to make two bit strings of equal length
int makeEqualLength(char *str1, char *str2) {
    int len1 = strlen(str1);
    int len2 = strlen(str2);
    if (len1 < len2) {
        int diff = len2 - len1;
        while (diff > 0) {
            memmove(str1 + 1, str1, len1 + 1);
            str1[0] = '0';
            len1++;
            diff--;
        }
        return len2;
    } else if (len1 > len2) {
        int diff = len1 - len2;
        while (diff > 0) {
            memmove(str2 + 1, str2, len2 + 1);
            str2[0] = '0';
            len2++;
            diff--;
        }
    }
    return len1; // If len1 >= len2
}

// Function to add two bit strings and return the result
char *addBitStrings(char *first, char *second) {
    int length = makeEqualLength(first, second);
    int carry = 0;
    static char result[100]; // Assuming a maximum size for result

    for (int i = length - 1; i >= 0; i--) {
        int firstBit = first[i] - '0';
        int secondBit = second[i] - '0';
        int sum = (firstBit ^ secondBit ^ carry) + '0';
        result[i + 1] = (char)sum;
        carry = (firstBit & secondBit) | (secondBit & carry) | (firstBit & carry);
    }

    if (carry) {
        result[0] = '1';
        return result;
    } else {
        return result + 1;
    }
}

// Function to multiply two single bits represented as characters '0' or '1'
int multiplySingleBit(char a, char b) {
    return (a - '0') * (b - '0');
}

// Function to multiply two bit strings and return the result as a long integer
long int multiply(char *X, char *Y) {
    int n = makeEqualLength(X, Y);

    if (n == 0) return 0;
    if (n == 1) return multiplySingleBit(X[0], Y[0]);

    int fh = n / 2;
    int sh = n - fh;

    char Xl[100], Xr[100], Yl[100], Yr[100];
    strncpy(Xl, X, fh);
    Xl[fh] = '\0';
    strcpy(Xr, X + fh);
    strncpy(Yl, Y, fh);
    Yl[fh] = '\0';
    strcpy(Yr, Y + fh);

    long int P1 = multiply(Xl, Yl);
    long int P2 = multiply(Xr, Yr);
    long int P3 = multiply(addBitStrings(Xl, Xr), addBitStrings(Yl, Yr));

    return P1 * (1 << (2 * sh)) + (P3 - P1 - P2) * (1 << sh) + P2;
}

// Driver program to test the multiplication function
int main() {
    printf("%ld\n", multiply("1100", "1010"));
    printf("%ld\n", multiply("110", "1010"));
    printf("%ld\n", multiply("11", "1010"));
    printf("%ld\n", multiply("1", "1010"));
    printf("%ld\n", multiply("0", "1010"));
    printf("%ld\n", multiply("111", "111"));
    printf("%ld\n", multiply("11", "11"));

    return 0;
}
