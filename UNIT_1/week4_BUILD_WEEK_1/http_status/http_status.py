# Esempio di utilizzo per eseguire la scansione di un server HTTP:
# python http_status_plus.py 192.168.1.1 80 /
#############################################################################

import http.client  # Importa la libreria per le connessioni HTTP
import logging  # Importa la libreria per il logging degli eventi
import sys  # Importa la libreria per gestire gli argomenti da riga di comando


def setup_logging():
    """
    Configura il sistema di logging.

    Crea un file di log "http_status.log" per memorizzare i log.
    """
    log_filename = "http_status.log"  # Nome del file di log
    logging.basicConfig(
        filename=log_filename,  # Configura il file di log
        level=logging.INFO,  # Imposta il livello di logging su INFO
        format="%(asctime)s - %(levelname)s - %(message)s",
    )  # Definisce il formato del log
    logging.info(
        "\n\nStarting new session\nLog file created"
    )  # Registra un messaggio di avvenuta creazione del file


def scan_http_methods(target_ip, port=80, path="/"):
    """
    Scansiona i metodi HTTP supportati dal server target.

    Parameters:
        target_ip (str): L'indirizzo IP del server target.
        port (int): Il numero di porta per connettersi (predefinito è 80).
        path (str): Il percorso da richiedere sul server (predefinito è '/').

    Returns:
        dict: Un dizionario con i metodi HTTP come chiavi e il loro stato come valori.
    """
    methods = [
        "OPTIONS",
        "GET",
        "HEAD",
        "POST",
        "PUT",
        "DELETE",
        "TRACE",
        "CONNECT",
        "PATCH",
        "PROPFIND",
        "PROPPATCH",
        "LOCK",
        "UNLOCK",
        "MOVE",
        "COPY",
        "LIST",
        "ADD",
        "REMOVE",
    ]  # Metodi HTTP da testare
    results = {}  # Dizionario per memorizzare i risultati della scansione

    for method in methods:  # Itera sui metodi HTTP
        try:
            connection = http.client.HTTPConnection(
                target_ip, port
            )  # Crea una connessione HTTP
            connection.request(
                method, path
            )  # Invia la richiesta HTTP con il metodo corrente
            response = connection.getresponse()  # Ottiene la risposta dal server
            status = response.status  # Ottiene lo stato della risposta

            if (
                200 <= status <= 299
            ):  # Se lo stato è tra 200 e 299, il metodo è abilitato
                results[method] = "Enabled"
            elif (
                300 <= status <= 399
            ):  # Se lo stato è tra 300 e 399, il metodo è attivo con reindirizzamento
                results[method] = "Active with redirection"
            elif (
                status >= 400
            ):  # Se lo stato è uguale o superiore a 400, il metodo è disabilitato
                results[method] = "Disabled"

            connection.close()
            logging.info(
                f"Metodo {method} all'indirizzo {target_ip}:{port}{path} - {results[method]}"
            )  # Registra il risultato nel file di log
        except Exception as e:  # Gestisce le eccezioni
            results[method] = (
                f"Error: {str(e)}"  # Registra l'errore nel dizionario dei risultati
            )
            logging.error(
                f"Metodo {method} all'indirizzo {target_ip}:{port}{path} - {results[method]}"
            )  # Registra il risultato nel file di log
    return results


def main():
    """
    Funzione principale per gestire l'input dell'utente ed eseguire la scansione dei metodi HTTP.
    """
    setup_logging()  # Configura il logging

    if len(sys.argv) < 2:  # Verifica se il numero di argomenti è sufficiente
        print(
            "Usage: python http_status_plus.py <target_ip> [port] [path]"
        )  # Stampa il messaggio di utilizzo
        print(
            "Example: python http_status_plus.py 192.168.1.1 80 /"
        )  # Fornisce un esempio di utilizzo
        logging.error("Invalid arguments provided")  # Registra un errore
        sys.exit(1)  # Termina il programma con un codice di errore
    target_ip = sys.argv[1]  # Ottiene l'IP target da riga di comando

    port = (
        int(sys.argv[2]) if len(sys.argv) > 2 else 80
    )  # Ottiene il numero di porta da riga di comando, default a 80
    path = (
        sys.argv[3] if len(sys.argv) > 3 else "/"
    )  # Ottiene il percorso, default a "/"
    print(
        f"Scanning HTTP methods on {target_ip}:{port}{path}"
    )  # Stampa messaggio inizio scansione
    logging.info(f"Starting scan on {target_ip}:{port}{path}")
    results = scan_http_methods(target_ip, port, path)  # Esegue la scansione
    logging.info("Scan completed")  # Registra la fine della scansione

    print("\nHTTP methods status:")  # Stampa l'intestazione dei risultati
    for method, status in results.items():  # Itera sui risultati
        print(f"{method}: {status}")  # Stampa ogni metodo e il suo stato
        logging.info(f"{method}: {status}")  # Registra ogni metodo/stato nel log


if __name__ == "__main__":  # Verifica se lo script è eseguito direttamente
    main()  # Chiama la funzione principale
