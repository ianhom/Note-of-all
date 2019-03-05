
//统计字符串中"O"的得分，连续的"O"累计加分，例如OXO为2分，OOX为3分 

#include <stdio.h>

int cnt=0,score=0;
void main(int argc, char **argv)
{
     char *s=argv[1];
     while(*s!='\0')
     {
         if(*s++=='O')score+=(++cnt);
         else cnt=0;
     }
     printf("The String is %s\nThe score is %d\n",argv[1],score);
}
