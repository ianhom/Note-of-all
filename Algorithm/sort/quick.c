#include <stdio.h>

void qsort(int *a, int l, int r)
{
    if(l>=r)
        return;
    int i=l,j=r,x=a[i];
    while(i<j)
    {
        while(i<j && s[j]>=x)
            j--;
        s[i]=s[j];
        
    }
}
