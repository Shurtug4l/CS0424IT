#include <stdio.h>
#include <string.h>

int main() {
  char str1[100], str2[100];

  // Input dell'utente per due stringhe
  printf("Inserisci la prima stringa: ");
  fgets(str1, sizeof(str1), stdin);
  str1[strcspn(str1, "\n")] = 0; // Rimuove il carattere di newline
  printf("Inserisci la seconda stringa: ");
  fgets(str2, sizeof(str2), stdin);
  str2[strcspn(str2, "\n")] = 0; // Rimuove il carattere di newline

  // Confronto delle stringhe
  if (strcmp(str1, str2) == 0) {
    printf("Le stringhe sono uguali.\n");
  } else {
    printf("Le stringhe sono diverse.\n");
  }

  // Concatenazione delle stringhe
  char result[200];
  strcpy(result, str1); // Copia str1 in result
  strcat(result, str2); // Aggiunge str2 a result

  // Stampa la stringa concatenata
  printf("La stringa concatenata è: %s\n", result);

  return 0;
}
