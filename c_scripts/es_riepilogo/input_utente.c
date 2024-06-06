#include <stdio.h>

int main() {
  int num1, num2;

  // Input dell'utente
  printf("Inserisci due numeri interi: ");
  scanf("%d %d", &num1, &num2);

  // Somma dei numeri inseriti
  int somma = num1 + num2;
  printf("La somma di %d e %d è %d\n", num1, num2, somma);

  return 0;
}
