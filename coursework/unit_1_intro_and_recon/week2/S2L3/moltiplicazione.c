/*
Il programma include la libreria standard \texttt{stdio.h} necessaria per le
operazioni di input/output.
*/
#include <stdio.h>

/*
La funzione main inizia dichiarando una variabile product inizializzata a 1.0
per il calcolo del prodotto e una variabile choice per memorizzare la scelta
dell'utente.
*/
int main()
{
  float product = 1.0f; // Inizializza il prodotto a 1.0 per la moltiplicazione
  char choice;

  /*
  Il programma utilizza un ciclo do-while per chiedere all'utente di inserire un
  numero. Se l'input non è un numero valido, viene visualizzato un messaggio di
  errore e l'input buffer viene pulito.
  */
  do
  {
    float number;

    printf("Inserisci un numero in virgola mobile (o 'q' per uscire): ");
    if (scanf("%f", &number) != 1)
    { // Controlla se scanf ha avuto successo
      fprintf(
          stderr,
          "Errore: Input non valido. Per favore inserisci un numero o 'q'.\n");
      // Svuota il buffer di input per prevenire comportamenti inattesi
      while ((getchar()) != '\n')
        ;
      continue;
    }
    // Se l'utente inserisce 0, il programma visualizza un avviso che il
    // risultato sarà 0.
    if (number == 0.0f)
    {
      printf("Attenzione: Moltiplicando per 0 si otterrà 0.\n");
    }
    // Il numero inserito viene moltiplicato al prodotto corrente.
    product *= number;
    // Il programma chiede all'utente se vuole inserire un altro numero e
    // continua il ciclo se la risposta è 'y' o 'Y'.
    printf("Vuoi inserire un altro numero (y/n)? ");
    scanf(" %c", &choice);
  } while (choice == 'y' || choice == 'Y');
  // Alla fine del ciclo, il programma visualizza il prodotto di tutti i numeri
  // inseriti e termina.
  printf("Il prodotto di tutti i numeri inseriti è: %.5f\n", product);

  return 0;
}
