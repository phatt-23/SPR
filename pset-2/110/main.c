#include<stdio.h>

int main()
{
    char a[10] = "a";
    for (int i = 0; i < sizeof(a)/sizeof(*a); i++)
        putchar(a[i]);

    return 0;
}
