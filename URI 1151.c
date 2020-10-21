#include "stdio.h"
 
int main()
{
  int a, b, aux, i, n;
  a = 0;
  b = 1;
 
  printf("Digite um número: ");
  scanf("%d", &n);
  printf("Série de Fibonacci:\n");
  printf("%d\n", b);

  for(i = 0; i < n; i++)
  {
    aux = a + b;
    a = b;
    b = aux;
 
    printf("%d\n", aux);
  }
}