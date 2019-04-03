#include <stdio.h>
void main(int argc, char **argv)
{
    int ret=0,cnt=0;
    char *s=argv[1];
    while(*s!='\0')
        if(*s++=='O')ret+=(++cnt);
        else cnt=0;
    printf("The score is %d\n",ret);
}
