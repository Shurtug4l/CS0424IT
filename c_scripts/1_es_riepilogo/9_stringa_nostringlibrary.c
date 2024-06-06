#include <stdio.h>

// Funzione per trovare la lunghezza della stringa
int stringLength(char *str) {
  int length = 0;
  while (str[length] != '\0') {
    length++;
  }
  return length;
}

// Funzione per confrontare due stringhe
int stringCompare(char *str1, char *str2) {
  int i = 0;
  while (str1[i] != '\0' && str2[i] != '\0') {
    if (str1[i] != str2[i]) {
      return str1[i] - str2[i];
    }
    i++;
  }
  return str1[i] - str2[i];
}

// Funzione per copiare una stringa
void stringCopy(char *dest, char *src) {
  int i = 0;
  while (src[i] != '\0') {
    dest[i] = src[i];
    i++;
  }
  dest[i] = '\0';
}

// Funzione per concatenare due stringhe
void stringConcat(char *dest, char *src) {
  int destLen = stringLength(dest);
  int i = 0;
  while (src[i] != '\0') {
    dest[destLen + i] = src[i];
    i++;
  }
  dest[destLen + i] = '\0';
}

int main() {
  char str1[100], str2[100];

  // Input dell'utente per due stringhe
  printf("Inserisci la prima stringa: ");
  fgets(str1, sizeof(str1), stdin);
  if (str1[stringLength(str1) - 1] == '\n') {
    str1[stringLength(str1) - 1] = '\0'; // Rimuove il carattere di newline
  }
  printf("Inserisci la seconda stringa: ");
  fgets(str2, sizeof(str2), stdin);
  if (str2[stringLength(str2) - 1] == '\n') {
    str2[stringLength(str2) - 1] = '\0'; // Rimuove il carattere di newline
  }

  // Confronto delle stringhe
  if (stringCompare(str1, str2) == 0) {
    printf("Le stringhe sono uguali.\n");
  } else {
    printf("Le stringhe sono diverse.\n");
  }

  // Concatenazione delle stringhe
  char result[200];
  stringCopy(result, str1);   // Copia str1 in result
  stringConcat(result, str2); // Aggiunge str2 a result

  // Stampa la stringa concatenata
  printf("La stringa concatenata è: %s\n", result);

  return 0;
}
