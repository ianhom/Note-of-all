#include <stdio.h>
#include "my_lib.h"

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

void main(int argc, char **argv)
{
    int a[100];
    MY_ATOI_ARGV(a);
    qsort(a,0,sizeof(a)-1);
    for(int i=0;i<sizeof(a);i++)
        printf("%d,"a[i]);
    return;
}
