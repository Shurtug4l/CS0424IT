#include <stdio.h>
#include <string.h>

#define BUFFER_SIZE 10

int main() {
  char buffer[BUFFER_SIZE];
  char extra; // Variabile per controllare se l'input è troppo lungo

  printf("Si prega di inserire il nome utente: ");
  // Utilizziamo fgets per limitare l'input alla dimensione del buffer
  if (fgets(buffer, BUFFER_SIZE, stdin) != NULL) {
    // Controlliamo se l'input è troppo lungo
    if (buffer[strlen(buffer) - 1] != '\n') {
      // L'input è troppo lungo se fgets non legge il carattere newline
      printf("Errore: l'input è troppo lungo. Si prega di inserire un massimo "
             "di %d caratteri.\n",
             BUFFER_SIZE - 1);
      // Puliamo il buffer di input per evitare problemi con gli input
      // successivi
      while ((extra = getchar()) != '\n' && extra != EOF) {
        // Scartiamo i caratteri extra
      }
    } else {
      // Rimuoviamo il carattere di newline
      buffer[strlen(buffer) - 1] = '\0';
      printf("Nome utente inserito: %s\n", buffer);
    }
  } else {
    printf("Errore nella lettura dell'input.\n");
  }

  return 0;
}
