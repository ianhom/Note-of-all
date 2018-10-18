#include <stdio.h>

int a[10] = {7,3,4,1,2,6,8,5,9,0};
int i,j,t;

int bubble_sort(void)
{
    for(i = 0; i < 9; i++)
    {
        for(j = 0; j < 9-i; j++)
        {
            if(a[j] <= a[j+1])
            {
                t = a[j];
                a[j] = a[j+1];
                a[j+1] = t;
            }
        }
    }
    return 0;
}
