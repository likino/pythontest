#include <stdio.h>
int main(void)
{
	int i, j;
	for(i=9;i>=1;i--)
	{
		for(j=1;j<=9;j++)
		{
			if(j<i) printf("\t");
			else printf("%d\t",i * j);
		}
		printf("\n");
	}
}