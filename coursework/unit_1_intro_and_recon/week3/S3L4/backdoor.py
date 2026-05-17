# Importazione delle librerie necessarie
import os
import platform
import socket

# Definizione dell'indirizzo IP del server (lasciato vuoto per ascoltare su tutti gli IP disponibili)
SRV_ADDR = ""
# Definizione della porta su cui il server ascolterà le connessioni
SRV_PORT = 1234

# Creazione di un socket utilizzando IPv4 (AF_INET) e il protocollo TCP (SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Binding del socket all'indirizzo e alla porta specificati
s.bind((SRV_ADDR, SRV_PORT))
# Il server inizia ad ascoltare le connessioni in entrata, con una coda di connessioni pendenti pari a 1
s.listen(1)
# Accettazione di una connessione in entrata
connection, address = s.accept()

# Stampa un messaggio che indica che un client si è connesso, mostrando l'indirizzo del client
print("client connected: ", address)

# Loop infinito per mantenere la connessione aperta e gestire i comandi ricevuti
while 1:
    try:
        # Ricezione di dati dal client, con un buffer di 1024 byte
        data = connection.recv(1024)
    except:
        # Se c'è un errore nella ricezione, continua il loop senza interrompersi
        continue

    # Controllo del comando ricevuto dal client
    if data.decode("utf-8") == "1":
        # Se il comando è '1', raccoglie informazioni sul sistema operativo e l'architettura
        tosend = platform.platform() + " " + platform.machine()
        # Invia le informazioni raccolte al client
        connection.sendall(tosend.encode())
    elif data.decode("utf-8") == "2":
        # Se il comando è '2', tenta di elencare i file in una directory specificata dal client
        data = connection.recv(1024)
        try:
            # Ottiene la lista dei file nella directory specificata
            filelist = os.listdir(data.decode("utf-8"))
            tosend = ""
            # Crea una stringa contenente i nomi dei file, separati da una virgola
            for x in filelist:
                tosend += "," + x
        except:
            # Se c'è un errore (ad esempio, directory inesistente), imposta un messaggio di errore
            tosend = "Wrong path"
        # Invia la lista dei file o il messaggio di errore al client
        connection.sendall(tosend.encode())
    elif data.decode("utf-8") == "0":
        # Se il comando è '0', chiude la connessione corrente
        connection.close()
        # Accetta una nuova connessione
        connection, address = s.accept()
