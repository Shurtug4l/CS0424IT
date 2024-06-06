#include <stdio.h>

int main() {
  int num1, num2;

  // Input dell'utente per due numeri
  printf("Inserisci il primo numero: ");
  scanf("%d", &num1);
  printf("Inserisci il secondo numero: ");
  scanf("%d", &num2);

  // Determina il maggiore tra i due numeri
  if (num1 > num2) {
    printf("Il numero maggiore è: %d\n", num1);
  } else if (num2 > num1) {
    printf("Il numero maggiore è: %d\n", num2);
  } else {
    printf("I numeri sono uguali.\n");
  }

  return 0;
}
