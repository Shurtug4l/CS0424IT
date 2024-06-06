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

  // Verifica se le stringhe sono uguali
  if (strcmp(str1, str2) == 0) {
    printf("Le stringhe sono uguali.\n");
  } else {
    printf("Le stringhe sono diverse.\n");
  }

  return 0;
}
