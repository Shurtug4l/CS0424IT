#include <stdio.h>

int main() {
  int num1, num2;

  // Input dell'utente per due numeri
  printf("Inserisci il primo numero: ");
  scanf("%d", &num1);
  printf("Inserisci il secondo numero: ");
  scanf("%d", &num2);

  // Verifica se i numeri sono uguali
  if (num1 == num2) {
    printf("I numeri sono uguali.\n");
  } else {
    printf("I numeri sono diversi.\n");
  }

  return 0;
}
