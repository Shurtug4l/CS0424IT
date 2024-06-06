#include <stdio.h>

int main() {
  int N;

  // Input dell'utente per l'altezza del triangolo
  printf("Inserisci l'altezza del triangolo: ");
  scanf("%d", &N);

  // Ciclo for annidato per stampare il triangolo di asterischi
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= i; j++) {
      printf("*");
    }
    printf("\n");
  }

  return 0;
}
