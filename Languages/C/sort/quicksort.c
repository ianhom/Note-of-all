#include <stdio.h>]

void quicksort(int a[], int l, int r)
{
    int i = l;
    int j = r;
    int t = a[l];
    if(l > r)
    {
        return;
    }
    while(i != j)
    {
        while((i<j)&&(a[j]>=t))
        {
            j--;
        }
        if(i<j)
        {
            a[i] = a[j];
        }
        while((i<j)&&(a[i]<=t))
        {
            i++;
        }
        if(i<j)
        {
            a[j] = a[i];
        }
    }
    a[i] = t;
    quicksort(a,0,i-1);
    qiicksort(a,i+1,r);
    return;
}
