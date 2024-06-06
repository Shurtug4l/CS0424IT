#include <stdio.h>

int main() {
  int num;

  // Input dell'utente per il numero
  printf("Inserisci un numero: ");
  scanf("%d", &num);

  // Verifica se il numero è positivo e dispari
  if (num > 0 && num % 2 != 0) {
    printf("Il numero %d è positivo e dispari.\n", num);
  } else {
    printf("Il numero %d non è sia positivo che dispari.\n", num);
  }

  return 0;
}
