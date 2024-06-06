#include <stdio.h>

int main() {
  int cond1, cond2;

  // Input dell'utente per due valori booleani
  printf("Inserisci il primo valore booleano (0 o 1): ");
  scanf("%d", &cond1);
  printf("Inserisci il secondo valore booleano (0 o 1): ");
  scanf("%d", &cond2);

  // Verifica se almeno una delle condizioni è vera
  if (cond1 || cond2) {
    printf("Almeno una delle condizioni è vera.\n");
  } else {
    printf("Nessuna delle condizioni è vera.\n");
  }

  return 0;
}
