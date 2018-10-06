#include <stdio.h>

int func(int *A, int n)
{
    int i;
    int Max = A[0];
    int MaxTemp = A[0];
    for(i = 0; i < n; i++)
    {
        MaxTemp = max(A[i],MaxTemp+A[i]);
        Max     = max(Max,MaxTemp);
    }
    printf("%d",Max);
    return 0;
}
