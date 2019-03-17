//题目：从1到N自然数，将所有数字练起来，统计数字0~9出现的次数。

#include <stdio.h>
void cal(int a)
{
    n[a%10]++;
    cal(a/10)；
}


int n[10]={0};
void main(int argc, char **argv)
{
    int ret=0;
    char *s=argv[1];
    while(*s>='0'&&*s<='9')ret=ret*10+*s++-'0';
    for(int i=1; i<=ret;i++)
    {
     #if(1)
        cal(i);    //same way with while, but slower;
     #else
        int j=i;      
        do
        {
            n[j%10]++;
            j/=10;
        }while(j);
     #endif
    }
    for(int i=0;i<10;i++)
        printf("%d,",n[i]);
    printf("\n");
}
