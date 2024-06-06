#include <stdio.h>

int main() {
  int num;

  // Input dell'utente per un numero
  printf("Inserisci un numero: ");
  scanf("%d", &num);

  // Verifica se il numero è uguale a zero
  if (num == 0) {
    printf("Il numero è uguale a zero.\n");
  } else {
    printf("Il numero non è uguale a zero.\n");
  }

  return 0;
}
