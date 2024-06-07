### Memoria e Stack in C

**Qual è la differenza principale tra stack e heap nella gestione della memoria in C?**  
A) Lo stack è gestito dal programmatore, mentre l'heap è gestito dal sistema operativo.
B) Lo stack è utilizzato per le variabili locali e i parametri delle funzioni, mentre l'heap è utilizzato per la memoria dinamica.
C) Lo stack cresce verso l'alto, mentre l'heap cresce verso il basso.
D) Lo stack è utilizzato solo per i puntatori, mentre l'heap è utilizzato solo per gli array.
Risposta corretta: B​​
- Lo stack viene utilizzato per gestire le variabili locali e i parametri delle funzioni in modo automatico, con allocazione e deallocazione gestite dal sistema. L'heap, invece, viene utilizzato per la memoria dinamica, che deve essere allocata e deallocata esplicitamente dal programmatore tramite funzioni come `malloc` e `free`.

**Quale operazione viene eseguita per aggiungere un elemento sulla cima dello stack?**
A) POP
B) PUSH
C) INSERT
D) ADD
Risposta corretta: B​​
- L'operazione PUSH aggiunge un elemento in cima allo stack, mentre POP è l'operazione che rimuove l'elemento più in alto.

**Quale operazione viene utilizzata per rimuovere l'elemento più in alto dello stack?**
A) REMOVE
B) DELETE
C) POP
D) DROP
Risposta corretta: C
- L'operazione POP rimuove l'elemento in cima allo stack, liberando la memoria allocata per l'elemento.

**Cosa rappresenta l'acronimo LIFO, utilizzato per descrivere il comportamento dello stack?**
A) Last In First Out
B) Last In First Only
C) Last In Fast Out
D) Last In Fixed Order
Risposta corretta: A
- LIFO significa "Last In First Out", che indica che l'ultimo elemento aggiunto allo stack sarà il primo a essere rimosso.

**Quale dei seguenti puntatori indica la base dello stack di una funzione chiamata?**
A) EIP
B) ESP
C) EBP
D) EAX
Risposta corretta: C
- Il puntatore EBP (Base Pointer) punta alla base dello stack della funzione chiamata, aiutando nell'accesso ai parametri e variabili locali.

**Qual è la funzione del puntatore ESP nello stack?**
A) Indica l'istruzione corrente.
B) Indica la cima dello stack.
C) Indica la base dello stack.
D) Indica il prossimo indirizzo di memoria libero.
Risposta corretta: B
- Il puntatore ESP (Stack Pointer) indica la cima dello stack, gestendo l'allocazione e deallocazione della memoria dello stack.

### Puntatori e Arrays in C

**Come si dichiara un puntatore a un intero in C?**
A) int ptr;
B) int *ptr;
C) int &ptr;
D) int ptr*;
Risposta corretta: B​​
- La dichiarazione `int *ptr;` definisce un puntatore che può memorizzare l'indirizzo di una variabile di tipo intero. Gli altri non sono sintatticamente corretti per dichiarare un puntatore a intero.

**Quale tipo di dato viene usato per dichiarare una variabile che punta a un intero in C?**
A) int
B) *int
C) int*
D) pointer int
Risposta corretta: C
- La dichiarazione `int*` viene utilizzata per definire un puntatore a un intero, con `*` che indica il tipo puntatore.

**Qual è la funzione del comando scanf in C?**
A) Scrivere un messaggio sulla console.
B) Leggere l'input dell'utente dalla tastiera.
C) Allocare memoria dinamicamente.
D) Terminare l'esecuzione di un programma.
Risposta corretta: B​​
- La funzione `scanf` viene utilizzata per leggere l'input dell'utente dalla tastiera, permettendo di acquisire dati in vari formati.

**Quale delle seguenti dichiarazioni crea un array di 10 interi?**
A) int array[10];
B) int array(10);
C) int array{10};
D) int array.10;
Risposta corretta: A​​
- La dichiarazione `int array[10];` crea un array di 10 interi. Le altre opzioni non sono sintatticamente valide per dichiarare un array in C.

**Quale dei seguenti è un esempio di dichiarazione corretta di un array bidimensionale in C?**
A) int matrix[2,3];
B) int matrix[2][3];
C) int matrix(2)(3);
D) int matrix{2}{3};
Risposta corretta: B​​
- La dichiarazione `int matrix[2][3];` definisce un array bidimensionale con 2 righe e 3 colonne. Le altre opzioni non sono sintatticamente valide in C.

**Quale delle seguenti affermazioni descrive correttamente gli array multidimensionali in C?**
A) Un array con un singolo indice.
B) Un array con due o più indici.
C) Un array che può contenere qualsiasi tipo di dato.
D) Un array che utilizza puntatori per l'accesso ai dati.
Risposta corretta: B
- Un array multidimensionale è un array che utilizza due o più indici per accedere ai suoi elementi, come un array bidimensionale `int matrix[2][3];`.

### Operatori e Funzioni in C

**Quale operatore aritmetico in C viene utilizzato per calcolare il resto della divisione tra due numeri?**
A) /
B) %
C) //
D) &
Risposta corretta: B​​
- L'operatore `%` calcola il resto della divisione tra due numeri interi.

**Quale delle seguenti affermazioni è corretta riguardo le funzioni di tipo void in C?**
A) Le funzioni di tipo void non possono ricevere parametri.
B) Le funzioni di tipo void non restituiscono alcun valore.
C) Le funzioni di tipo void devono sempre includere l'istruzione return.
D) Le funzioni di tipo void possono restituire qualsiasi tipo di dato.
Risposta corretta: B​​
- Le funzioni di tipo void non restituiscono alcun valore. Possono comunque ricevere parametri e non è obbligatorio includere l'istruzione `return`.

**Qual è la funzione principale del comando scanf in C?**
A) Scrivere un messaggio sulla console.
B) Leggere l'input dell'utente dalla tastiera.
C) Allocare memoria dinamicamente.
D) Terminare l'esecuzione di un programma.
Risposta corretta: B​​
- La funzione `scanf` è utilizzata per leggere l'input dell'utente dalla tastiera.

**Quale tipo di dato in C è rappresentato da %f nelle funzioni printf e scanf?**
A) int
B) float
C) char
D) double
Risposta corretta: B​​
- `%f` rappresenta il tipo di dato `float`, utilizzato per numeri con virgola mobile.

**Quale operatore logico in C viene utilizzato per verificare se due condizioni sono entrambe vere?**
A) ||
B) &&
C) !
D) ==
Risposta corretta: B​​
- L'operatore `&&` verifica se entrambe le condizioni sono vere. `||` verifica se almeno una delle condizioni è vera, `!` nega la condizione, e `==` confronta l'uguaglianza tra due valori.

**Quale operatore in C viene utilizzato per incrementare il valore di una variabile di 1?**
A) --
B) ++
C) +=
D) -+
Risposta corretta: B​​
- L'operatore `++` incrementa il valore di una variabile di 1. L'operatore `--` decrementa il valore, `+=` aggiunge un valore specificato, e `-+` non è un operatore valido.

### Gestione della Memoria Dinamica in C

**Quale dei seguenti comandi viene usato per allocare dinamicamente memoria in C?**
A) malloc
B) calloc
C) realloc
D) Tutti i precedenti
Risposta corretta: D
- Le funzioni `malloc`, `calloc` e `realloc` sono utilizzate per allocare dinamicamente la memoria in C.

**Quale delle seguenti è una pratica comune per prevenire i memory leaks in un programma C?**
A) Allocare sempre più memoria del necessario per evitare overflow.
B) Deallocare esplicitamente tutta la memoria allocata dinamicamente utilizzando free().
C) Utilizzare solo variabili globali per evitare confusione con la memoria locale.
D) Evitare l'uso di puntatori e array.
Risposta corretta: B​​
- Deallocare esplicitamente tutta la memoria allocata dinamicamente utilizzando `free()` è essenziale per prevenire i memory leaks. Allocare più memoria del necessario, evitare puntatori e usare solo variabili globali non sono pratiche corrette per prevenire i memory leaks.

### Errori e Sicurezza in C

**In un programma C, cosa succede se si cerca di accedere a un indice di un array al di fuori dei suoi limiti?**
A) Il compilatore genera un errore di sintassi.
B) Viene generato un errore di runtime che interrompe immediatamente il programma.
C) Viene restituito un valore di default (ad esempio 0 per gli interi).
D) Si verifica un comportamento indefinito che può portare a un crash o a dati corrotti.
Risposta corretta: D​​
- Accedere a un indice di un array al di fuori dei suoi limiti causa un comportamento indefinito, che può portare a un crash del programma o a dati corrotti.

**Quale dei seguenti errori non viene rilevato dal compilatore durante la compilazione del codice C?**
A) Errori di sintassi
B) Errori di esecuzione
C) Errori di dichiarazione
D) Errori di tipo
Risposta corretta: B​​
- Gli errori di runtime (esecuzione) non vengono rilevati dal compilatore; si verificano durante l'esecuzione del programma. Gli errori di sintassi, dichiarazione e tipo sono rilevati dal compilatore.

### Funzioni e Strutture di Controllo in C

**Quale delle seguenti istruzioni di controllo permette di eseguire blocchi di codice diversi basati su molteplici condizioni?**
A) if-else
B) switch
C) for
D) while
Risposta corretta: B​​
- La struttura `switch` permette di eseguire blocchi di codice diversi basati su molteplici condizioni, utilizzando `case` per specificare le condizioni.

**Quale delle seguenti è la struttura corretta di una funzione che restituisce un valore intero in C?**
A) int funzione(int a, int b) { return a + b; }
B) void funzione(int a, int b) { return a + b; }
C) funzione(int a, int b) { return a + b; }
D) int funzione(int a, int b) { a + b; return; }
Risposta corretta: A​​
- La struttura `int funzione(int a, int b) { return a + b; }` è corretta per una funzione che restituisce un valore intero. Le altre opzioni sono errate per vari motivi, come il tipo di ritorno sbagliato o la mancanza di dichiarazione del tipo di ritorno.

**In quale delle seguenti situazioni è appropriato utilizzare un ciclo do-while in C?**
A) Quando si vuole che il ciclo venga eseguito almeno una volta.
B) Quando non si conosce il numero esatto di iterazioni a priori.
C) Quando si vuole controllare la condizione all'inizio del ciclo.
D) Quando si vuole evitare l'uso di un puntatore.
Risposta corretta: A​​
- Il ciclo `do-while` viene utilizzato quando si vuole che il ciclo venga eseguito almeno una volta, poiché la condizione viene controllata alla fine del ciclo.

### Firewall e Sicurezza della Rete

**Qual è la funzione principale di un firewall nella sicurezza informatica?**
A) Crittografare i dati.
B) Controllare e regolamentare il traffico di rete.
C) Eseguire scansioni antivirus.
D) Gestire gli account utente.
Risposta corretta: B
- Un firewall controlla e regolamenta il traffico di rete per proteggere la rete da accessi non autorizzati.

**Quale dei seguenti è un tipo di firewall che monitora le connessioni di rete per permettere o bloccare il traffico?**
A) Packet Filtering
B) Stateful Filtering
C) Proxy Firewall
D) Application Firewall
Risposta corretta: B
- Il firewall stateful monitoring tiene traccia delle connessioni attive per determinare quali pacchetti di rete permettere o bloccare.

**Qual è la funzione di un Intrusion Detection System (IDS)?**
A) Bloccare automaticamente tutte le minacce.
B) Monitorare il traffico di rete e segnalare attività sospette.
C) Crittografare le comunicazioni di rete.
D) Eseguire il backup dei dati di rete.
Risposta corretta: B
- Un IDS monitora il traffico di rete e segnala attività sospette per rilevare possibili intrusioni.

**In che modo un Intrusion Prevention System (IPS) differisce da un IDS?**
A) Un IPS non monitora il traffico di rete.
B) Un IPS può bloccare o prevenire attacchi attivi.
C) Un IDS è più sicuro di un IPS.
D) Un IDS può bloccare attacchi attivi mentre un IPS non può.
Risposta corretta: B
- Un IPS può bloccare o prevenire attacchi attivi, mentre un IDS si limita a rilevare e segnalare.

**Quale delle seguenti tecniche è utilizzata per filtrare il traffico in base a criteri statici come indirizzi IP e porte?**
A) Stateful Filtering
B) Proxy Filtering
C) Packet Filtering
D) Dynamic Filtering
Risposta corretta: C
- Il packet filtering filtra il traffico in base a criteri statici come indirizzi IP e porte.

**Quale delle seguenti tecniche di filtraggio tiene traccia delle connessioni attive per migliorare la sicurezza?**
A) Stateless Filtering
B) Application Filtering
C) Stateful Filtering
D) Context-Based Filtering
Risposta corretta: C
- Il stateful filtering tiene traccia delle connessioni attive per migliorare la sicurezza.

**Qual è l'obiettivo principale di un firewall perimetrale?**
A) Proteggere dispositivi individuali all'interno della rete.
B) Controllare il traffico tra la rete interna e Internet.
C) Monitorare e registrare tutte le attività dei dipendenti.
D) Fornire servizi di autenticazione utente.
Risposta corretta: B
- Il firewall perimetrale controlla il traffico tra la rete interna e Internet per proteggere la rete interna da minacce esterne.

**Cosa rappresenta la "DMZ" in una rete?**
A) Una zona di rete interna sicura.
B) Una zona di rete esposta che offre servizi accessibili dall'esterno.
C) Un'area dedicata ai server di backup.
D) Un segmento di rete utilizzato solo per lo sviluppo software.
Risposta corretta: B
- La DMZ (Demilitarized Zone) è una zona di rete esposta che offre servizi accessibili dall'esterno, come i server web.

**Quale dei seguenti dispositivi è comunemente utilizzato per proteggere le diverse zone di una rete segmentata?**
A) Switch
B) Router
C) Firewall
D) Modem
Risposta corretta: C
- I firewall sono comunemente utilizzati per proteggere le diverse zone di una rete segmentata.

**Quale delle seguenti aree di rete è tipicamente esposta a Internet in un'architettura di rete aziendale?**
A) Intranet
B) DMZ
C) Sala server
D) Sala amministratori
Risposta corretta: B
- La DMZ è tipicamente esposta a Internet e offre servizi accessibili dall'esterno.

**Quale termine descrive una zona di rete che ospita servizi accessibili dall'esterno, come un sito di e-commerce?**
A) Intranet
B) Extranet
C) DMZ
D) LAN
Risposta corretta: C
- La DMZ ospita servizi accessibili dall'esterno.

**Quale dei seguenti dispositivi è utilizzato per implementare un firewall perimetrale?**
A) Router
B) Switch
C) Server
D) Firewall hardware
Risposta corretta: D
- Un firewall hardware è utilizzato per implementare un firewall perimetrale.

**Cosa rappresenta il termine 'multi-tier DMZ' in una rete aziendale?**
A) Una singola zona di rete per tutti i server.
B) Una rete con più livelli di sicurezza per proteggere i server esposti a Internet.
C) Un'area di rete dedicata ai backup.
D) Una rete senza firewall.
Risposta corretta: B
- Una 'multi-tier DMZ' è una rete con più livelli di sicurezza per proteggere i server esposti a Internet.

**Quale area della rete dovrebbe essere particolarmente protetta sia a livello di rete che fisicamente?**
A) Intranet
B) DMZ
C) Sala server
D) Sala client
Risposta corretta: C
- La sala server dovrebbe essere particolarmente protetta sia a livello di rete che fisicamente.

**Quale delle seguenti affermazioni è vera riguardo la segmentazione della rete?**
A) Riduce la complessità della rete.
B) Aumenta la sicurezza isolando aree della rete.
C) Elimina la necessità di firewall.
D) Riduce la velocità di trasmissione dei dati.
Risposta corretta: B
- La segmentazione della rete migliora la sicurezza isolando diverse aree della rete, riducendo il rischio di attacchi che si propagano attraverso la rete.

**Qual è l'azione comune per rimuovere un elemento dallo stack in un contesto di gestione della memoria?**
A) PUSH
B) POP
C) DELETE
D) REMOVE
Risposta corretta: B
- L'operazione POP rimuove un elemento dallo stack, liberando la memoria allocata per l'elemento.

**Qual è la funzione della policy che si trova alla fine di ogni policy set di un firewall?**
A) Permettere tutto il traffico non gestito dalle regole precedenti.
B) Bloccare tutto il traffico non gestito dalle regole precedenti.
C) Notificare all'amministratore tutto il traffico non gestito.
D) Resettare tutto il traffico non gestito.
Risposta corretta: B
- La policy alla fine di ogni policy set di un firewall tipicamente blocca tutto il traffico non gestito dalle regole precedenti, come misura di sicurezza di default.

**Qual è la funzione principale della segmentazione della rete in una struttura aziendale?**
A) Aumentare la velocità di trasmissione dei dati.
B) Ridurre il numero di dispositivi necessari.
C) Migliorare la sicurezza isolando diverse aree della rete.
D) Eliminare la necessità di firewall.
Risposta corretta: C​​
- La segmentazione della rete migliora la sicurezza isolando diverse aree della rete, limitando il movimento laterale degli attacchi e proteggendo le risorse critiche.
