#include <stdio.h>

// Dichiarazione della funzione per calcolare il fattoriale
int fattoriale(int n);

int main() {
  int num;

  // Input dell'utente
  printf("Inserisci un numero per calcolare il fattoriale: ");
  scanf("%d", &num);

  // Calcolo e stampa del fattoriale
  printf("Il fattoriale di %d è %d\n", num, fattoriale(num));

  return 0;
}

// Definizione della funzione per calcolare il fattoriale
int fattoriale(int n) {
  if (n == 0) {
    return 1;
  } else {
    return n * fattoriale(n - 1);
  }
}
