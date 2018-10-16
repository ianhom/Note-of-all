#define MAX 5
int n = MAX;
int a[MAX][MAX] = {{1,0,0,0,0},
                     {2,1,0,0,0},
                     {3,2,1,0,0},
                     {4,3,2,1,0},
                     {5,4,3,2,1}}; 
int dp[MAX][MAX]= {{0,0,0,0,0},
                     {0,0,0,0,0},
                     {0,0,0,0,0},
                     {0,0,0,0,0},
                     {0,0,0,0,0}};  
                     
int max(int a, int b)
{
    if(a > b)
        return b;
    else
        return a;
}

int main(void)
{    
    int i,j;

    for(i=0;i<n;i++)
    {
        dp[n-1][i]=a[n-1][i];
    }
    for(i=n-2;i>=0;i--)   
    {
        for(j=0;j<=i;j++)
        {
            dp[i][j]=max(dp[i+1][j],dp[i+1][j+1])+a[i][j];
        }
    }
    printf("%d\n",dp[0][0]);
    return 0；
}
