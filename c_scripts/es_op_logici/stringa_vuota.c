#include <stdio.h>
#include <string.h>

int main() {
  char str[100];

  // Input dell'utente per la stringa
  printf("Inserisci una stringa: ");
  fgets(str, sizeof(str), stdin);
  str[strcspn(str, "\n")] = 0; // Rimuove il carattere di newline

  // Verifica se la stringa è vuota
  if (strlen(str) == 0) {
    printf("La stringa è vuota.\n");
  } else {
    printf("La stringa non è vuota.\n");
  }

  return 0;
}
