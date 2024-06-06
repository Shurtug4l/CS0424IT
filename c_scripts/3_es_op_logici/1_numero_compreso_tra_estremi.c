#include <stdio.h>

int main() {
  int num, estremo1, estremo2;

  // Input dell'utente per il numero e gli estremi
  printf("Inserisci il numero da verificare: ");
  scanf("%d", &num);
  printf("Inserisci il primo estremo: ");
  scanf("%d", &estremo1);
  printf("Inserisci il secondo estremo: ");
  scanf("%d", &estremo2);

  // Verifica se il numero è compreso tra i due estremi
  if (num >= estremo1 && num <= estremo2) {
    printf("Il numero %d è compreso tra %d e %d.\n", num, estremo1, estremo2);
  } else {
    printf("Il numero %d non è compreso tra %d e %d.\n", num, estremo1,
           estremo2);
  }

  return 0;
}
