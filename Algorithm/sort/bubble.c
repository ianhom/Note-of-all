#include <stdio>

int atoi(char *s)
{
    int l,f,ret=0;
    if(0!=s)
        for(l=0;s[l]!='\0';l++);
    for(int i=0;i<l;i++)
    {
        if(s[i]>'9' || s[i] <'0')
        {  
            printf("Invalid input!\n");
            return 0;
        }
        f=1;
        for(int j=0;j<l-1-i;j++)
            f*=10;
        ret+=(s[i]-'0')*f;
    }
    return ret;
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
