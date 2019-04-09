```c
static int sa=234;
void main(void)
{
    int a=123;
    test();
    printf("a is %d\n",a);
}

void test(void)
{
    static int sb;
    int *p=(int*)&p; // Get SP value
    for(int i=0;i<20;i++)
        if(*(p+i)==123)
            *(p+i)=456;
    p=&sb;
    for(int i=-20;i<20;i++)
        if(*(p+i)==234)
            *(p+i)=789;
}
```
-
