- 通过指针寻找函数内不可见的全局变量及上层函数的局部变量，该方法比较危险，容易造成死机
```c
#include<stdio.h>
static int sa=234;
void main(void)
{
    int a=123;
    test();
    printf("a is %d\n",a);   // you get 456
    printf("sa is %d\n",sa); // you get 789
}

void test(void)
{
    static int sb;
    int *p=(int*)&p; // Get SP value
    for(int i=0;i<20;i++)
        if(*(p+i)==123)
            *(p+i)=456;
    p=&sa;
    for(int i=-20;i<20;i++)
        if(*(p+i)==234)
            *(p+i)=789;
}
```
