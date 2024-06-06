#include <stdio.h>
#include <string.h>

int main() {
  char str[100];

  // Input dell'utente per la stringa
  printf("Inserisci una stringa: ");
  fgets(str, sizeof(str), stdin);
  str[strcspn(str, "\n")] = 0; // Rimuove il carattere di newline

  // Ciclo for per stampare i singoli caratteri della stringa
  for (int i = 0; i < strlen(str); i++) {
    printf("%c\n", str[i]);
  }

  return 0;
}
