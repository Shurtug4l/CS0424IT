import hashlib
import itertools
import string
import time

# Hash delle password da craccare
hashes_to_crack = [
    "e99a18c428cb38d5f260853678922e03",
]


# Funzione per craccare con dictionary attack
def dictionary_attack(hash_to_crack, wordlist):
    start_time = time.time()
    with open(wordlist, "r", encoding="utf-8", errors="ignore") as file:
        for word in file:
            word = word.strip()
            hash_object = hashlib.md5(word.encode())
            hashed_word = hash_object.hexdigest()
            if hashed_word == hash_to_crack:
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(
                    f"Dictionary attack ha trovato la password: {word} in {elapsed_time:.2e} secondi"
                )
                return word, elapsed_time
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Dictionary attack non ha trovato la password in {elapsed_time:.2e} secondi")
    return None, elapsed_time


# Funzione per craccare con brute-force attack
def brute_force_attack(hash_to_crack, max_length=6):
    start_time = time.time()
    chars = string.printable
    attempt = 0
    for length in range(1, max_length + 1):
        for guess in itertools.product(chars, repeat=length):
            guess = "".join(guess)
            attempt += 1
            print(f"Attempt {attempt}: Trying {guess}")
            hash_object = hashlib.md5(guess.encode())
            hashed_guess = hash_object.hexdigest()
            if hashed_guess == hash_to_crack:
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(
                    f"Brute-force attack ha trovato la password: {guess} in {elapsed_time:.2e} secondi"
                )
                return guess, elapsed_time
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(
        f"Brute-force attack non ha trovato la password in {elapsed_time:.2e} secondi"
    )
    return None, elapsed_time


# Funzione per craccare con rule-based attack
def rule_based_attack(hash_to_crack, wordlist):
    start_time = time.time()
    with open(wordlist, "r", encoding="utf-8", errors="ignore") as file:
        for word in file:
            word = word.strip()
            # Prova la parola originale
            if hashlib.md5(word.encode()).hexdigest() == hash_to_crack:
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(
                    f"Rule-based attack ha trovato la password: {word} in {elapsed_time:.2e} secondi"
                )
                return word, elapsed_time
            # Prova con alcune regole
            for i in range(10):
                modified_word = word + str(i)
                if hashlib.md5(modified_word.encode()).hexdigest() == hash_to_crack:
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    print(
                        f"Rule-based attack ha trovato la password: {modified_word} in {elapsed_time:.2e} secondi"
                    )
                    return modified_word, elapsed_time
                modified_word = str(i) + word
                if hashlib.md5(modified_word.encode()).hexdigest() == hash_to_crack:
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    print(
                        f"Rule-based attack ha trovato la password: {modified_word} in {elapsed_time:.2e} secondi"
                    )
                    return modified_word, elapsed_time
            # Aggiungere altre regole se necessario
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Rule-based attack non ha trovato la password in {elapsed_time:.2e} secondi")
    return None, elapsed_time


def main():
    # Chiedi all'utente quale metodo di attacco vuole usare
    method = (
        input("Inserisci il metodo di attacco (dictionary, brute_force, rule_based): ")
        .strip()
        .lower()
    )

    # Chiedi all'utente il percorso della wordlist se necessario
    wordlist = ""
    if method in ["dictionary", "rule_based"]:
        wordlist = input("Inserisci il percorso del file della wordlist: ").strip()

    # Chiedi la lunghezza massima per il brute-force se necessario
    max_length = 6
    if method == "brute_force":
        max_length = int(
            input(
                "Inserisci la lunghezza massima per il brute-force (consigliato 6): "
            ).strip()
        )

    # File di output per i risultati
    output_file = "cracked_passwords.txt"

    # Esegui il cracking delle password con il metodo selezionato
    with open(output_file, "w") as f:
        for hash_value in hashes_to_crack:
            cracked_password = None
            elapsed_time = 0

            if method == "dictionary":
                cracked_password, elapsed_time = dictionary_attack(hash_value, wordlist)

            elif method == "brute_force":
                cracked_password, elapsed_time = brute_force_attack(
                    hash_value, max_length
                )

            elif method == "rule_based":
                cracked_password, elapsed_time = rule_based_attack(hash_value, wordlist)

            f.write(f"Hash: {hash_value}\n")
            f.write(f"Metodo: {method.capitalize()} attack\n")
            f.write(
                f"Password: {cracked_password if cracked_password else 'Non trovata'}\n"
            )
            f.write(f"Tempo impiegato: {elapsed_time:.2e} secondi\n")
            f.write("\n")

    print("Risultati salvati su", output_file)


if __name__ == "__main__":
    main()
