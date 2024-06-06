#include <stdio.h>

int main() {
  int num1, num2, num3;

  // Input dell'utente per tre numeri
  printf("Inserisci il primo numero: ");
  scanf("%d", &num1);
  printf("Inserisci il secondo numero: ");
  scanf("%d", &num2);
  printf("Inserisci il terzo numero: ");
  scanf("%d", &num3);

  // Determina il maggiore tra i tre numeri
  if (num1 >= num2 && num1 >= num3) {
    printf("Il numero maggiore è: %d\n", num1);
  } else if (num2 >= num1 && num2 >= num3) {
    printf("Il numero maggiore è: %d\n", num2);
  } else {
    printf("Il numero maggiore è: %d\n", num3);
  }

  return 0;
}
