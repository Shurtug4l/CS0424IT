#include <stdio.h>

int main() {
  int num;

  // Input dell'utente per il numero
  printf("Inserisci un numero: ");
  scanf("%d", &num);

  // Verifica se il numero è pari
  if (num % 2 == 0) {
    printf("Il numero %d è pari.\n", num);
  } else {
    printf("Il numero %d è dispari.\n", num);
  }

  return 0;
}
