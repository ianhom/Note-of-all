//题目：从1到N自然数，将所有数字练起来，统计数字0~9出现的次数。
//分析：简单做法就是挨个循环统计，进阶就是摸索规律，最快的方法就是先计算一次n，然后把所有的结果都保存下来，下一次直接查表。
#include <stdio.h>
void cal(int a)
{
    n[a%10]++; 
    cal(a/10);//迭代方法
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
        cal(i);    //same way with while, but slower, because of function calling;
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
