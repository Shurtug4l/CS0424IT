#include <stdio.h>

int main() {
  char char1, char2;

  // Input dell'utente per due caratteri
  printf("Inserisci il primo carattere: ");
  scanf(" %c", &char1);
  printf("Inserisci il secondo carattere: ");
  scanf(" %c", &char2);

  // Determina l'ordine alfabetico tra i due caratteri
  if (char1 < char2) {
    printf("%c viene prima di %c nell'ordine alfabetico.\n", char1, char2);
  } else if (char1 > char2) {
    printf("%c viene dopo %c nell'ordine alfabetico.\n", char1, char2);
  } else {
    printf("I caratteri sono uguali.\n");
  }

  return 0;
}
