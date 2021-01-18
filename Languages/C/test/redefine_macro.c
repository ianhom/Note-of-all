#include <stdio.h>

#define MAX 10  // Fisrt define here
void test(void)
{
    printf("The MAX is %d in test()\r\n",MAX);
}

#define MAX 20  // redeine warning here
void main(void)
{
    printf("The MAX is %d in main()\r\n",MAX);
    test();
}