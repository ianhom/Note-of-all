#include <stdio.h>

#define N  10000
int n[10]={0};
void main(int argc, char **argv)
{
    for(int i=1; i<=N;i++)
    {
        int j=i;
        
        do
        {
            n[j%10]++;
            j/=10;
        }while(j);
    }
    for(int i=0;i<10;i++)
        printf("%d,",n[i]);
}
