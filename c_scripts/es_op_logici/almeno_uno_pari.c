#include <stdio.h>

int main() {
  int numeri[5];
  int trovato_pari = 0;

  // Input dell'utente per 5 numeri interi
  printf("Inserisci 5 numeri interi:\n");
  for (int i = 0; i < 5; i++) {
    scanf("%d", &numeri[i]);
  }

  // Verifica se almeno uno dei numeri è pari
  for (int i = 0; i < 5; i++) {
    if (numeri[i] % 2 == 0) {
      trovato_pari = 1;
      break;
    }
  }

  if (trovato_pari) {
    printf("Almeno uno dei numeri è pari.\n");
  } else {
    printf("Nessuno dei numeri è pari.\n");
  }

  return 0;
}
