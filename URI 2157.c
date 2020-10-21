#include <stdio.h>

int main ()
{
    int num, num1, i, j, x;
	int aux, aux2;
	scanf("%d", &x);

	while (x--)
	{
		scanf("%d %d", &num, &num1);
		for (i = num; i <= num1; i++)
			printf("%d", i);
		for (i = num1; i >= num; i--)
		{
			aux = i;
			while (aux)
			{
				aux2 = aux%10;
				printf("%d", aux2);
				aux = aux/10;
			}
		}	
		printf("\n");
	}
}