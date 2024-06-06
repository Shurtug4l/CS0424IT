#include <stdio.h>

int main() {
  // Dichiarazione e inizializzazione di un array
  int numeri[] = {1, 2, 3, 4, 5};
  int somma = 0;
  int lunghezza = sizeof(numeri) / sizeof(numeri[0]);

  // Calcolo della somma degli elementi dell'array
  for (int i = 0; i < lunghezza; i++) {
    somma += numeri[i];
  }

  // Calcolo della media
  float media = (float)somma / lunghezza;
  printf("La media degli elementi nell'array è %.2f\n", media);

  return 0;
}
