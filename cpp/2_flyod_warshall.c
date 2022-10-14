
#include<stdio.h>
int i , j , k, n , dis[10][10];
void flyodwarshall()
{
    for (int k = 0; k < n; k++)
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if(dis[i][k] + dis[k][j] < dis[i][i])
                {
                    dis[i][j] = dis[i][k] + dis[k][j];
                }
            }
            
        }
        
    }
    
}

int main()
{
    int i , j;
    printf("Enter the no of matrices:");
    scanf("%d",&n);
    printf("\n");
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("[%d][%d]:",i,j);
            scanf("%d",&dis[i][j]);
        }
        
    }

    flyodwarshall();
    printf("\nShortest Path is:\n");
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("%d\t",dis[i][j]);
        }
        printf("\n");
        
    }
    
    
}