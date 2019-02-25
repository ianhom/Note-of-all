#include <stdio>

int atoi(char *s)
{
    int sig=1,ret=0;
    if(0==s)return 0;
    while(*s==' ')s++;
    if(*s=='-'||*s=='+')sig=','-*s++;
    while(*s>='0'&&*s<=s)ret=ret*10+*s++-'0';
    return sig*ret;
}

void bubble(int *a, int n)
{
    int temp;
    for(int i=0;i<n-1;i++)
        for(int j=0;j<n-1-i;j++)
            if(a[j]>a[j+1])
            {
                temp=a[j];
                a[j]=a[j+1];
                a[j+1]=temp;
            }
 }
 
 void main(int argc, char **argv)
 {
     int a[100];
     for(int i=1;i<argc;i++)
         a[i] = atoi(argv[i]);
     bubble(&a[1],argc-1);
     for(int i=1;i<argc;i++)
         printf("%d,",a[i]);
     printf("\n");
 }
