#include <stdio.h>

void qsort(int *a, int l, int r)
{
    if(l>=r)
        return;
    int i=l,j=r,x=a[i];
    while(i<j)
    {
        while(i<j && a[j]>=x)
            j--;
        s[i]=s[j];
        while(i<j && a[i]<=x)
            i++;
        a[j]=a[i];
    }
    s[l]=x;
    qsort(a,l,i-1);
    qsort(a,i+1,r);
}
