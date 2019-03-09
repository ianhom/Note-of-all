```c
for(int l=0;s[l]!='\0';l++); //get length of string.
```

```c
int a[3][3]={{1,2,3},{4,5,6},{7,8,9}};
int hash=0;
for(int i=0;i<3;i++)
    for(int j=0;j<3;j++)
    {
        hash+=(a[i][j]&0x01);
        hash<<=2;
    }
```
