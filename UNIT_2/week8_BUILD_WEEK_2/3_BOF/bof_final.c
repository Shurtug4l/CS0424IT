#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Funzione che provoca un segmentation fault accedendo a indici fuori dai
// limiti
void cause_segmentation_fault()
{
  int vector[10];
  int i;
  int min = 1;
  int max = 200;
  int random_number;

  // Inizializza il generatore di numeri casuali
  srand(time(NULL));

  for (i = 0; i < 1000000; i++)
  {
    random_number = rand() % (max - min + 1) + min;
    // Questo causerà eventualmente un segmentation fault
    printf("[%d]:", i);
    printf("%d\n", random_number);
    vector[i] =
        random_number; // Tentativo di accesso fuori dai limiti intenzionalmente
  }
}

// Funzione per l'esecuzione normale del programma
void normal_execution()
{
  int vector[10], i, j, k;
  int swap_var;

  printf("Inserire 10 interi:\n");

  for (i = 0; i < 10; i++)
  {
    int c = i + 1;
    printf("[%d]:", c);

    // Controllo dell'input per assicurarsi che l'utente inserisca un numero
    // intero
    while (scanf("%d", &vector[i]) != 1)
    {
      printf("Input non valido! Inserisci un numero intero.\n");
      while (getchar() != '\n')
        ; // Svuota il buffer dell'input
      printf("[%d]:", c);
    }
  }

  // Stampa il vettore inserito
  printf("Il vettore inserito è:\n");
  for (i = 0; i < 10; i++)
  {
    int t = i + 1;
    printf("[%d]: %d\n", t, vector[i]);
  }

  // Bubble sort per ordinare il vettore
  for (j = 0; j < 10 - 1; j++)
  {
    for (k = 0; k < 10 - j - 1; k++)
    {
      if (vector[k] > vector[k + 1])
      {
        swap_var = vector[k];
        vector[k] = vector[k + 1];
        vector[k + 1] = swap_var;
      }
    }
  }

  // Stampa il vettore ordinato
  printf("Il vettore ordinato è:\n");
  for (j = 0; j < 10; j++)
  {
    int g = j + 1;
    printf("[%d]: %d\n", g, vector[j]);
  }
}

int main()
{
  int choice;

  // Menu di scelta per l'utente
  printf("Menu:\n");
  printf("1. Esegui normalmente\n");
  printf("2. Causa segmentation fault con accesso casuale\n");
  printf("3. Esci\n");
  printf("Inserisci la tua scelta: ");

  // Controllo dell'input dell'utente per una scelta valida
  while (scanf("%d", &choice) != 1 || (choice < 1 || choice > 3))
  {
    printf("Scelta non valida! Inserisci 1, 2 o 3: ");
    while (getchar() != '\n')
      ; // Svuota il buffer dell'input
  }

  // Gestione delle diverse scelte dell'utente
  if (choice == 2)
  {
    cause_segmentation_fault();
  }
  else if (choice == 1)
  {
    normal_execution();
  }
  else if (choice == 3)
  {
    printf("Uscita dal programma.\n");
    return 0; // Esci dal programma
  }

  return 0;
}
