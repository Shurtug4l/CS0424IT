#include <stdio.h>
#include <stdlib.h>

// Dichiarazione della funzione per calcolare il fattoriale
unsigned long long fattoriale(unsigned long long n);

int main() {
  unsigned long long num;
  unsigned long long risultato;

  // Input dell'utente
  printf("Inserisci un numero per calcolare il fattoriale: ");
  scanf("%llu", &num);

  // Avviso all'utente se il numero è negativo e conversione al valore assoluto
  if ((long long)num < 0) {
    printf("Hai inserito un numero negativo. Verrà considerato il valore assoluto.\n");
    num = llabs((long long)num);
  }

  // Calcolo e stampa del fattoriale
  risultato = fattoriale(num);
  printf("Il fattoriale di %llu è %llu\n", num, risultato);

  return 0;
}

// Definizione della funzione per calcolare il fattoriale
unsigned long long fattoriale(unsigned long long n) {
  if (n == 0) {
    return 1;
  } else {
    return n * fattoriale(n - 1);
  }
}
