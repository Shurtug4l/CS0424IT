import logging
import socket
from datetime import datetime


class UDPServer:
    def __init__(self, ip_ascolto, porta_ascolto):
        """Inizializzazione del server UDP con IP e porta di ascolto."""
        self.ip_ascolto = ip_ascolto
        self.porta_ascolto = porta_ascolto
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.ip_ascolto, self.porta_ascolto))

    def avvia_server(self):
        """Avvia il server UDP e inizia ad ascoltare i pacchetti in arrivo."""
        logging.info(f"Server in ascolto su {self.ip_ascolto}:{self.porta_ascolto}")
        while True:
            try:
                dati, addr = self.socket.recvfrom(1024)  # Riceve dati fino a 1024 byte
                logging.info(f"Ricevuto pacchetto da {addr}: {dati}")
                self.socket.sendto(
                    b"Pacchetto ricevuto", addr
                )  # Invia conferma di ricezione
            except Exception as e:
                logging.error(f"Errore durante la ricezione del pacchetto: {e}")


def configura_logging():
    """Configura il logging per l'applicazione."""
    nome_file_log = f"udp_server_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
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


def main():
    configura_logging()
    logging.info("Avvio del server UDP")

    ip_ascolto = "0.0.0.0"  # Ascolta su tutte le interfacce di rete
    porta_ascolto = 20002  # Porta di ascolto del server

    server = UDPServer(ip_ascolto, porta_ascolto)
    server.avvia_server()


if __name__ == "__main__":
    main()
