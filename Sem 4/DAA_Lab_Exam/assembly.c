#include <stdio.h>

int min(int a, int b) {
    return a < b ? a : b;
}

int fun(int a[][4], int t[][4], int cl, int cs, int x1, int x2, int n) {
    if (cs == n - 1) {
        if (cl == 0) {
            return x1;
        } else {
            return x2;
        }
    }

    int same = fun(a, t, cl, cs + 1, x1, x2, n) + a[cl][cs + 1];
    int diff = fun(a, t, !cl, cs + 1, x1, x2, n) + a[!cl][cs + 1] + t[cl][cs + 1];

    return min(same, diff);
}

int main() {
    int n = 4;
    int a[2][4] = { { 4, 5, 3, 2 }, { 2, 10, 1, 4 } };
    int t[2][4] = { { 0, 7, 4, 5 }, { 0, 9, 2, 8 } };

    int e1 = 10;
    int e2 = 12;
    int x1 = 18;
    int x2 = 7;

    int x = fun(a, t, 0, 0, x1, x2, n) + e1 + a[0][0];
    int y = fun(a, t, 1, 0, x1, x2, n) + e2 + a[1][0];

    printf("%d\n", min(x, y));

    return 0;
}
