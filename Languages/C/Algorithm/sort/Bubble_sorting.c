#include <stdio.h>

int n;
scanf("%d",&n);
int i,j,t;
int ar[n];
for(i=0;i<n;i++)
    scanf("%d",&ar[i]);
for(i = 0; i < n; i++)
    {
        for(j = 0; j < n-i; j++)
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
