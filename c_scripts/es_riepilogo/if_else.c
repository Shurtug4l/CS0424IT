#include <stdio.h>

int main() {
  int num;

  // Input dell'utente
  printf("Inserisci un numero: ");
  scanf("%d", &num);

  // Controllo se il numero è positivo, negativo o zero
  if (num > 0) {
    printf("Il numero è positivo.\n");
  } else if (num < 0) {
    printf("Il numero è negativo.\n");
  } else {
    printf("Il numero è zero.\n");
  }

  return 0;
}
