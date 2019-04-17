- 通过指针寻找函数内不可见的全局变量及上层函数的局部变量，该方法比较危险，容易造成死机，原理上是通过局部函数内可见的局部变量或静态局部变量来搜索外部变量
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
-  设计数据结构的时候，可以从每个个体的视角将数据组织起来，然后充分利用这些数据进行处理，然后再除去无用到位视角。
