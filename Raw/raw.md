```c
void main(void)
{
    int a=123;
    test();
    printf("a is %d\n",a);
}

void test(void)
{
    int *p=(int*)&p; // Get SP value
    for(int i=0;i<20;i++)
        if(*(p+i)==123)
            *(p+i)=456;
}
```
