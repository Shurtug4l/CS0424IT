### Memoria e Stack in C

**Qual è la differenza principale tra stack e heap nella gestione della memoria in C?**
Risposta corretta: B​​
- Lo stack è utilizzato per le variabili locali e i parametri delle funzioni, mentre l'heap è utilizzato per la memoria dinamica. Lo stack cresce automaticamente con l'allocazione di variabili locali e deallocazione al termine della funzione, mentre l'heap richiede una gestione esplicita tramite funzioni come `malloc` e `free`.

**Quale operazione viene eseguita per aggiungere un elemento sulla cima dello stack?**
Risposta corretta: B​​
- L'operazione PUSH aggiunge un elemento in cima allo stack, mentre POP rimuove l'elemento più in alto.

**Quale operazione viene utilizzata per rimuovere l'elemento più in alto dello stack?**
Risposta corretta: C
- L'operazione POP rimuove l'elemento in cima allo stack.

**Cosa rappresenta l'acronimo LIFO, utilizzato per descrivere il comportamento dello stack?**
Risposta corretta: A
- LIFO sta per "Last In First Out", indicando che l'ultimo elemento aggiunto allo stack sarà il primo a essere rimosso.

**Quale dei seguenti puntatori indica la base dello stack di una funzione chiamata?**
Risposta corretta: C
- Il puntatore EBP (Base Pointer) punta alla base dello stack della funzione chiamata, facilitando l'accesso ai parametri e variabili locali della funzione.

**Qual è la funzione del puntatore ESP nello stack?**
Risposta corretta: B
- Il puntatore ESP (Stack Pointer) indica la cima dello stack, monitorando l'allocazione e deallocazione della memoria dello stack.

### Puntatori e Arrays in C

**Come si dichiara un puntatore a un intero in C?**
Risposta corretta: B​​
- La dichiarazione `int *ptr;` definisce un puntatore che può memorizzare l'indirizzo di una variabile di tipo intero.

**Quale tipo di dato viene usato per dichiarare una variabile che punta a un intero in C?**
Risposta corretta: C
- La dichiarazione `int*` viene utilizzata per definire un puntatore a un intero.

**Qual è la funzione del comando scanf in C?**
Risposta corretta: B​​
- La funzione `scanf` viene utilizzata per leggere l'input dell'utente dalla tastiera.

**Quale delle seguenti dichiarazioni crea un array di 10 interi?**
Risposta corretta: A​​
- La dichiarazione `int array[10];` crea un array di 10 interi.

**Quale dei seguenti è un esempio di dichiarazione corretta di un array bidimensionale in C?**
Risposta corretta: B​​
- La dichiarazione `int matrix[2][3];` definisce un array bidimensionale con 2 righe e 3 colonne.

**Quale delle seguenti affermazioni descrive correttamente gli array multidimensionali in C?**
Risposta corretta: B
- Un array multidimensionale è un array che utilizza due o più indici per accedere ai suoi elementi.

### Operatori e Funzioni in C

**Quale operatore aritmetico in C viene utilizzato per calcolare il resto della divisione tra due numeri?**
Risposta corretta: B​​
- L'operatore `%` calcola il resto della divisione tra due numeri.

**Quale delle seguenti affermazioni è corretta riguardo le funzioni di tipo void in C?**
Risposta corretta: B​​
- Le funzioni di tipo void non restituiscono alcun valore.

**Qual è la funzione principale del comando scanf in C?**
Risposta corretta: B​​
- La funzione `scanf` è utilizzata per leggere l'input dell'utente dalla tastiera.

**Quale tipo di dato in C è rappresentato da %f nelle funzioni printf e scanf?**
Risposta corretta: B​​
- `%f` rappresenta il tipo di dato `float`.

**Quale operatore logico in C viene utilizzato per verificare se due condizioni sono entrambe vere?**
Risposta corretta: B​​
- L'operatore `&&` verifica se entrambe le condizioni sono vere.

**Quale operatore in C viene utilizzato per incrementare il valore di una variabile di 1?**
Risposta corretta: B​​
- L'operatore `++` incrementa il valore di una variabile di 1.

### Gestione della Memoria Dinamica in C

**Quale dei seguenti comandi viene usato per allocare dinamicamente memoria in C?**
Risposta corretta: D
- Le funzioni `malloc`, `calloc` e `realloc` sono utilizzate per allocare dinamicamente la memoria.

**Quale delle seguenti è una pratica comune per prevenire i memory leaks in un programma C?**
Risposta corretta: B​​
- Deallocare esplicitamente tutta la memoria allocata dinamicamente utilizzando `free()` è essenziale per prevenire i memory leaks.

### Errori e Sicurezza in C

**In un programma C, cosa succede se si cerca di accedere a un indice di un array al di fuori dei suoi limiti?**
Risposta corretta: D​​
- Si verifica un comportamento indefinito che può portare a un crash o a dati corrotti.

**Quale dei seguenti errori non viene rilevato dal compilatore durante la compilazione del codice C?**
Risposta corretta: B​​
- Gli errori di runtime non vengono rilevati dal compilatore; si verificano durante l'esecuzione del programma.

### Funzioni e Strutture di Controllo in C

**Quale delle seguenti istruzioni di controllo permette di eseguire blocchi di codice diversi basati su molteplici condizioni?**
Risposta corretta: B​​
- La struttura `switch` permette di eseguire blocchi di codice diversi basati su molteplici condizioni.

**Quale delle seguenti è la struttura corretta di una funzione che restituisce un valore intero in C?**
Risposta corretta: A​​
- La struttura `int funzione(int a, int b) { return a + b; }` è corretta per una funzione che restituisce un valore intero.

**In quale delle seguenti situazioni è appropriato utilizzare un ciclo do-while in C?**
Risposta corretta: A​​
- Quando si vuole che il ciclo venga eseguito almeno una volta, è appropriato utilizzare un ciclo `do-while`.

### Firewall e Sicurezza della Rete

**Qual è la funzione principale di un firewall nella sicurezza informatica?**
Risposta corretta: B
- Un firewall controlla e regolamenta il traffico di rete per proteggere la rete da accessi non autorizzati.

**Quale dei seguenti è un tipo di firewall che monitora le connessioni di rete per permettere o bloccare il traffico?**
Risposta corretta: B
- Il firewall stateful monitoring tiene traccia delle connessioni attive per determinare quali pacchetti di rete permettere o bloccare.

**Qual è la funzione di un Intrusion Detection System (IDS)?**
Risposta corretta: B
- Un IDS monitora il traffico di rete e segnala attività sospette.

**In che modo un Intrusion Prevention System (IPS) differisce da un IDS?**
Risposta corretta: B
- Un IPS può bloccare o prevenire attacchi attivi, mentre un IDS si limita a rilevare e segnalare.

**Quale delle seguenti tecniche è utilizzata per filtrare il traffico in base a criteri statici come indirizzi IP e porte?**
Risposta corretta: C
- Il packet filtering filtra il traffico in base a criteri statici come indirizzi IP e porte.

**Quale delle seguenti tecniche di filtraggio tiene traccia delle connessioni attive per migliorare la sicurezza?**
Risposta corretta: C
- Il stateful filtering tiene traccia delle connessioni attive per migliorare la sicurezza.

**Qual è l'obiettivo principale di un firewall perimetrale?**
Risposta corretta: B
- Il firewall perimetrale controlla il traffico tra la rete interna e Internet per proteggere la rete interna da minacce esterne.

**Cosa rappresenta la "DMZ" in una rete?**
Risposta corretta: B
- La DMZ (Demilitarized Zone) è una zona di rete esposta che offre servizi accessibili dall'esterno, come i server web.

**Quale dei seguenti dispositivi è comunemente utilizzato per proteggere le diverse zone di una rete segmentata?**
Risposta corretta: C
- I firewall sono comunemente utilizzati per proteggere le diverse zone di una rete segmentata.

**Quale delle seguenti aree di rete è tipicamente esposta a Internet in un'architettura di rete aziendale?**
Risposta corretta: B
- La DMZ è tipicamente esposta a Internet e offre servizi accessibili dall'esterno.

**Quale termine descrive una zona di rete che ospita servizi accessibili dall'esterno, come un sito di e-commerce?**
Risposta corretta: C
- La DMZ ospita servizi accessibili dall'esterno.

**Quale dei seguenti dispositivi è utilizzato per implementare un firewall perimetrale?**
Risposta corretta: D
- Un firewall hardware è utilizzato per implementare un firewall perimetrale.

**Cosa rappresenta il termine 'multi-tier DMZ' in una rete aziendale?**
Risposta corretta: B
- Una 'multi-tier DMZ' è una rete con più livelli di sicurezza per proteggere i server esposti a Internet.

**Quale area della rete dovrebbe essere particolarmente protetta sia a livello di rete che fisicamente?**
Risposta corretta: C
- La sala server dovrebbe essere particolarmente protetta sia a livello di rete che fisicamente.

**Quale delle seguenti affermazioni è vera riguardo la segmentazione della rete?**
Risposta corretta: C
- La segmentazione della rete migliora la sicurezza isolando diverse aree della rete.

**Qual è l'azione comune per rimuovere un elemento dallo stack in un contesto di gestione della memoria?**
Risposta corretta: B
- L'operazione POP rimuove un elemento dallo stack.

**Qual è la funzione della policy che si trova alla fine di ogni policy set di un firewall?**
Risposta corretta: B
- La policy alla fine di ogni policy set di un firewall tipicamente blocca tutto il traffico non gestito dalle regole precedenti.

**Qual è la funzione principale della segmentazione della rete in una struttura aziendale?**
Risposta corretta: C​​
- La segmentazione della rete migliora la sicurezza isolando diverse aree della rete.
