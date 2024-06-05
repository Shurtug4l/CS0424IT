/*
Inclusione delle librerie standard <stdio.h> per l'input/output, <math.h> per le
funzioni matematiche e <stdbool.h> per il supporto ai tipi booleani.
*/
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#define MAX_NUMBERS 100 // Numero massimo di input consentiti (100)

/*
La funzione get_float visualizza un prompt all'utente e legge un valore float.
Restituisce true se l'input è valido. Questa funzione prende due argomenti: un
prompt da visualizzare e un puntatore a float dove memorizzare il valore letto.
*/
bool get_float(const char *prompt, float *value) {
  printf("\n%s", prompt);
  return scanf("%f", value) == 1;
}

/*La funzione get_confirmation chiede all'utente una conferma (sì/no) e
 * restituisce true se la risposta è affermativa (y o Y). Questa funzione prende
 * un prompt da visualizzare come argomento.*/
bool get_confirmation(const char *prompt) {
  char answer;
  printf("%s (y/n): ", prompt);
  return scanf(" %c", &answer) == 1 && (answer == 'y' || answer == 'Y');
}

/*
La funzione calculate_statistics calcola la media, la mediana e la deviazione
standard di un array di numeri. Se il numero di elementi è zero, la funzione
restituisce immediatamente. Per calcolare la media, somma tutti i numeri e
divide per il numero di elementi.
*/
void calculate_statistics(float numbers[], int num_elements, float *mean,
                          float *median, float *standard_deviation) {
  if (num_elements == 0) {
    return; // gestisce NO input
  }

  *mean = 0.0f;
  for (int i = 0; i < num_elements; i++) {
    *mean += numbers[i];
  }
  *mean /= num_elements;

  /*
  Per calcolare la mediana, l 'array dei numeri viene ordinato utilizzando il
  bubble sort (per semplicità). La variabile swapped tiene traccia se ci sono
  stati scambi durante l' ordinamento.
  */
  bool swapped;
  do {
    swapped = false;
    for (int i = 0; i < num_elements - 1; i++) {
      if (numbers[i] > numbers[i + 1]) {
        float temp = numbers[i];
        numbers[i] = numbers[i + 1];
        numbers[i + 1] = temp;
        swapped = true;
      }
    }
  } while (swapped);

  /*
  La mediana viene calcolata in base al numero di elementi: se è pari, la
  mediana è la media dei due elementi centrali, altrimenti è il valore centrale.
  */
  if (num_elements % 2 == 0) {
    *median =
        (numbers[num_elements / 2 - 1] + numbers[num_elements / 2]) / 2.0f;
  } else {
    *median = numbers[num_elements / 2];
  }

  /*
  La deviazione standard viene calcolata sommando i quadrati delle differenze
  tra ogni numero e la media, quindi calcolando la radice quadrata della somma
  divisa per il numero di elementi.
   */
  *standard_deviation = 0.0f;
  for (int i = 0; i < num_elements; i++) {
    float deviation = numbers[i] - *mean;
    *standard_deviation += deviation * deviation;
  }
  *standard_deviation = sqrt(*standard_deviation / num_elements);
}

/*
La funzione main gestisce l'interazione con l'utente per ottenere i numeri.
Visualizza un messaggio di benvenuto, poi in un ciclo chiede all'utente di
inserire numeri fino a quando l'utente decide di smettere o si raggiunge il
numero massimo di input.
*/
int main() {
  float numbers[MAX_NUMBERS];
  int num_elements = 0;

  printf("Questo programma calcola la media, la mediana e la deviazione "
         "standard di un insieme di numeri.\n");

  do {
    float number;
    if (!get_float("Inserisci un numero (o 'q' per uscire): ", &number)) {
      fprintf(stderr, "Errore: Input non valido.\n");
      continue;
    }

    if (num_elements == MAX_NUMBERS) {
      fprintf(stderr,
              "Attenzione: Numero massimo di elementi raggiunto (%d).\n",
              MAX_NUMBERS);
      break;
    }

    numbers[num_elements++] = number;
  } while (get_confirmation("Aggiungere un altro numero?"));

  /*
  Se non sono stati inseriti numeri, il programma termina con un messaggio
  appropriato. Altrimenti, calcola e stampa le statistiche (media, mediana,
  deviazione standard) utilizzando la funzione calculate_statistics.
  */
  if (num_elements == 0) {
    printf("Nessun numero inserito.\n");
    return 0;
  }

  float mean, median, standard_deviation;
  calculate_statistics(numbers, num_elements, &mean, &median,
                       &standard_deviation);

  printf("\nStatistiche:\n");
  printf("  Numero di input:             %d\n", num_elements);
  printf("  Media:                         %.5f\n", mean);
  printf("  Mediana:                       %.5f\n", median);
  printf("  Deviazione standard:           %.5f\n", standard_deviation);

  return 0;
}
