#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define LEADERBOARD_FILE "leaderboard.txt"

typedef struct {
  char *domanda;
  char *opzioni[3];
  char rispostaCorretta;
} Domanda;

// Funzione per stampare la presentazione del gioco
void presentazioneGioco() {
  printf("************************************************\n");
  printf("*                                              *\n");
  printf("*      Benvenuto al quizzone astrofisico!      *\n");
  printf("*   Affronterai un quiz a risposta multipla    *\n");
  printf("* Avrai 3 scelte, solo una sarà quella giusta! *\n");
  printf("*                                              *\n");
  printf("************************************************\n\n\n\n");
}

// Funzione per stampare la schermata finale
void schermataFinale(int punteggio) {
  printf("************************************************\n");
  printf("*                                              *\n");
  printf("*              FINE DEL QUIZZONE!              *\n");
  printf("*            Complimenti, hai finito!          *\n");
  printf("*                                              *\n");
  printf("************************************************\n\n\n");
  printf("Il tuo punteggio finale e': %d/15\n\n\n", punteggio);
}

// Funzione per gestire una domanda
int gestisciDomanda(Domanda *domanda) {
  char risposta;
  printf("\n%s\n", domanda->domanda);
  printf("a) %s\nb) %s\nc) %s\n", domanda->opzioni[0], domanda->opzioni[1],
         domanda->opzioni[2]);
  printf("Inserisci la tua risposta (a, b o c): ");
  scanf(" %c", &risposta);
  if (risposta == domanda->rispostaCorretta) {
    printf("Esatto!\n\n");
    return 1;
  } else {
    printf("Sbagliato! La risposta corretta era %c) %s.\n\n",
           domanda->rispostaCorretta,
           (domanda->rispostaCorretta == 'a'
                ? domanda->opzioni[0]
                : (domanda->rispostaCorretta == 'b' ? domanda->opzioni[1]
                                                    : domanda->opzioni[2])));
    return 0;
  }
}

// Funzione per mescolare le domande
void mescola(Domanda *array, int n) {
  for (int i = n - 1; i > 0; i--) {
    int j = rand() % (i + 1);
    Domanda temp = array[i];
    array[i] = array[j];
    array[j] = temp;
  }
}

// Funzione per mostrare la leaderboard
void mostraLeaderboard() {
  FILE *file = fopen(LEADERBOARD_FILE, "r");
  // Se il file non esiste, apriamolo in modalità append per crearlo
  if (file == NULL) {
    file = fopen(LEADERBOARD_FILE, "a");
    if (file == NULL) {
      printf("Errore nella creazione del file leaderboard.\n\n\n");
      return;
    }
    fclose(file);
    // Ora riapriamo il file in modalità lettura
    file = fopen(LEADERBOARD_FILE, "r");
    if (file == NULL) {
      printf("Errore nell'apertura del file leaderboard.\n\n\n");
      return;
    }
  }

  printf("\n\n************************************************\n");
  printf("*                 LEADERBOARD                  *\n");
  printf("************************************************\n\n\n");

  char line[50];
  while (fgets(line, sizeof(line), file)) {
    printf("%s", line);
  }

  fclose(file);
}

// Funzione per aggiornare la leaderboard
void aggiornaLeaderboard(char *username, int punteggio) {
  FILE *file = fopen(LEADERBOARD_FILE, "a");
  if (file == NULL) {
    printf("Errore nell'apertura del file leaderboard.\n\n\n");
    return;
  }

  fprintf(file, "%s: %d/15\n", username, punteggio);
  fclose(file);
}

int main() {
  char risposta0, username[15];
  int punteggio = 0;

  // Presentazione gioco
  presentazioneGioco();

  do {
    // Scelta nuova partita o esci dal gioco
    printf("                                                \n");
    printf(" a) Nuova partita         b) Esci dal gioco     \n");
    printf(" c) Mostra leaderboard                         \n");
    printf("                                                \n");

    printf(" Inserisci la tua risposta: \n");
    scanf(" %c", &risposta0);

    if (risposta0 == 'a') {
      printf("Iniziamo una nuova partita!\n");

      // Prendiamo username giocatore
      printf("Inserisci il tuo username prima di iniziare: ");
      scanf("%s", username);
      printf("Grande %s, inziamo!\n", username);
      punteggio = 0;

      // Array delle domande, opzioni e risposte corrette
      Domanda domande[15] = {
          {"Qual è la stella più vicina alla Terra dopo il Sole?",
           {"Altair", "Alpha Centauri", "Betelgeuse"},
           'b'},
          {"Qual è il pianeta più grande del Sistema Solare?",
           {"Giove", "Saturno", "Urano"},
           'a'},
          {"Di che tipo è la nostra galassia?",
           {"Ellittica", "A spirale", "A spirale barrata"},
           'c'},
          {"Quale pianeta è conosciuto come la Stella del Mattino?",
           {"Venere", "Marte", "Mercurio"},
           'a'},
          {"Cosa sono i buchi neri?",
           {"Oggetti luminosi",
            "Regione di spazio-tempo con un campo gravitazionale così forte "
            "che nulla può sfuggire",
            "Stelle morenti"},
           'b'},
          {"Cos'è una supernova?",
           {"Nascita di una stella", "Esplosione di una stella",
            "Morte di un pianeta"},
           'b'},
          {"Qual è il pianeta più esterno del Sistema Solare?",
           {"Venere", "Urano", "Nettuno"},
           'c'},
          {"Quanti pianeti ci sono nel sistema solare?", {"7", "8", "9"}, 'b'},
          {"Qual è il nome della più grande luna di Saturno?",
           {"Titano", "Europa", "Ganimede"},
           'a'},
          {"Cos'è la Via Lattea?",
           {"Un sistema solare", "Una galassia", "Un pianeta"},
           'b'},
          {"Qual è il pianeta più vicino al Sole?",
           {"Venere", "Marte", "Mercurio"},
           'c'},
          {"Cosa sono le nebulose?",
           {"Regioni di spazio con una concentrazione di gas e polveri",
            "Agglomerati di stelle", "Stelle molto luminose"},
           'a'},
          {"Qual è l'elemento principale contenuto nelle stelle?",
           {"Elio", "Idrogeno", "Ossigeno"},
           'b'},
          {"Cos'è l'anno luce?",
           {"Unità di misura della distanza in astronomia", "Durata di un anno",
            "Velocità della luce"},
           'a'},
          {"Qual è la principale teoria che spiega l'origine dell'universo?",
           {"Teoria delle Stringhe", "Teoria del Big Bang",
            "Teoria della Relatività"},
           'b'}};

      // Mescolare le domande
      srand(time(NULL));
      mescola(domande, 15);

      // Gestione delle domande
      for (int i = 0; i < 15; i++) {
        punteggio += gestisciDomanda(&domande[i]);
      }

      // Schermata finale
      schermataFinale(punteggio);

      // Aggiornamento della leaderboard
      aggiornaLeaderboard(username, punteggio);
    } else if (risposta0 == 'c') {
      // Mostra leaderboard
      mostraLeaderboard();
    } else if (risposta0 != 'b') {
      printf("Scelta non valida. Riprova\n");
    } else {
      printf("Esci dal gioco. Ci vediamo alla prossima!\n");
    }

  } while (risposta0 != 'b');

  return 0;
}
