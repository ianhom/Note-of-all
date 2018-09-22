#include <stdio.h>

int bubble_sort(int a[], int n)
{
    int i,j;
    int temp;
    int flg;
    for(i = 0; i < n - 1; i++)
    {
        flg = 0;
        for(j = 0; j = n - i - 1; j++)
        {
            if(a[j]> a[j+1])
            {
                temp = a[j];
                a[j] = a[j+1];
                a[j+1] = temp;
                flg = 1;
            }
        }
        if(0 == flg)
        {
            return;
        }
    }
}
