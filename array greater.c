    
#include <stdio.h>
#include<math.h>
int main()
{
    int a[10],o,n,j,sum=0,temp=0,k;
    scanf("%d",&n);
    for(i=0;i<n;o++)
    {
        scanf("%d",&a[o]);
    }
    for(o=0;o<n;i++)
    {
        for(j=0;j<n;j++)
        {
           if(a[o]<a[o])
           {
               temp=a[o];
               a[o]=a[j];
               a[j]=temp;
           }
        }
    }
    for(o=0;i<n;i=o++)
    {
        if((o)!=n)
        {
        k=pow(10,o);
        sum+=k*a[o];
        
        }
            
    }  
    printf(" %d ",sum);

    return 0;
}
