#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int check_if_integer(char *str) {
  if (*str == '-' || *str == '+')
    str++; // Salta il segno
  if (!*str)
    return 0; // Stringa vuota dopo il segno non valida
  while (*str) {
    if (!isdigit(*str))
      return 0; // Se non è una cifra, ritorna 0
    str++;
  }
  return 1; // Tutti i caratteri sono cifre
}

// Funzione che provoca un segmentation fault accedendo a indici fuori dai
// limiti
void cause_segmentation_fault() {
  int vector[10];
  int i;
  int min = 1;
  int max = 100;
  int random_number;

  // Inizializza il generatore di numeri casuali
  srand(time(NULL));

  for (i = 0; i < 1000000; i++) {
    int length = sizeof(vector) / sizeof(vector[0]);
    if (i > length) {
      break;
    }

    random_number = rand() % (max - min + 1) + min;
    // Questo causerà eventualmente un segmentation fault
    printf("[%d]:", i);
    printf("%d\n", random_number);
    vector[i] = random_number; // Tentativo di accesso fuori dai limiti
  }
}

// Funzione per l'esecuzione normale del programma
void normal_execution() {
  int vector[10], i, j, k;
  int swap_var;
  char input[256];

  printf("\nInserire 10 interi:\n");

  for (i = 0; i < 10; i++) {
    int c = i + 1;
    printf("[%d]:", c);

    while (1) {
      scanf("%s", input);
      if (check_if_integer(input)) {
        vector[i] = atoi(input); // Conversione stringa -> intero
        break;                   // Uscita dal ciclo se input valido
      } else {
        printf("Input non valido! Inserisci un numero intero.\n");
        printf("[%d]:", c);
      }
    }
  }

  // Stampa il vettore inserito
  printf("\nIl vettore inserito è:\n");
  for (i = 0; i < 10; i++) {
    int t = i + 1;
    printf("[%d]: %d\n", t, vector[i]);
  }

  // Bubble sort per ordinare il vettore
  for (j = 0; j < 10 - 1; j++) {
    for (k = 0; k < 10 - j - 1; k++) {
      if (vector[k] > vector[k + 1]) {
        swap_var = vector[k];
        vector[k] = vector[k + 1];
        vector[k + 1] = swap_var;
      }
    }
  }

  // Stampa il vettore ordinato
  printf("\nIl vettore ordinato è:\n");
  for (j = 0; j < 10; j++) {
    int g = j + 1;
    printf("[%d]: %d\n", g, vector[j]);
  }
}

int main() {
  int choice;
  char input[256];

  // Menu di scelta per l'utente
  printf("\nMenu:\n");
  printf("1. Esegui normalmente\n");
  printf("2. Causa segmentation fault con accesso casuale\n");
  printf("3. Esci\n");

  while (1) {
    printf("Inserisci la tua scelta: ");
    scanf("%s", input);
    if (check_if_integer(input)) {
      choice = atoi(input);
      if (choice >= 1 && choice <= 3) {
        break;
      }
    }
    printf("Scelta non valida! Inserisci 1, 2 o 3: ");
  }

  // Gestione delle diverse scelte dell'utente
  if (choice == 1) {
    normal_execution();
  } else if (choice == 2) {
    cause_segmentation_fault();
  } else if (choice == 3) {
    printf("Uscita dal programma.\n");
    return 0; // Esci dal programma
  }

  return 0;
}
