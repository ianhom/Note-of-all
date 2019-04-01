#include<stdio.h>
void main(int argc, char **argv)
{
    int score=0;
    int cnt=0;
    int *s=argv[1];
    while(*s != '\0')
    {
        if(*s=='O')score+=(++cnt);
        else cnt=0;
    }
    printf("The score is %d\n",score);
}
