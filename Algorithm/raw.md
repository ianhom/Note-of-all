```c
for(int l=0;s[l]!='\0';l++); //get length of string.
```

```c
#include <stdio.h>

int a[3][3]={{1,2,3},{4,5,6},{7,8,9}};
int b[3][3]={{9,2,2},{3,6,4},{19,2,0}};

int hash(int a[3][3])
{
    int hash=0;
    for(int i=0;i<3;i++)
        for(int j=0;j<3;j++)
        {
            hash+=(a[i][j]&0x01);
            hash<<=2;
        }
    return hash;
}
void main(void)
{
    printf("hash 1 is %d\nhash 2 is %d",hash(a),hash(b));
}
```
- 通过hash表将链表优化，分散链表的起点，使在链表结构中查找更为快捷
