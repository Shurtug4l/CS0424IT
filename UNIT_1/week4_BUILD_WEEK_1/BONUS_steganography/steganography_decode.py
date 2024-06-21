from PIL import Image


# Funzione per convertire una stringa di bit in un messaggio di testo
def bits_to_message(bits):
    message = ""
    for i in range(0, len(bits), 8):
        byte = bits[i : i + 8]  # Prende 8 bit alla volta
        if byte == "00000000":  # Il carattere nullo indica la fine del messaggio
            break
        message += chr(int(byte, 2))  # Converte la stringa di bit in un carattere
    return message


# Funzione per estrarre un messaggio nascosto da un'immagine
def extract_message(image_path):
    image = Image.open(image_path)  # Carica l'immagine
    pixels = list(image.getdata())  # Ottiene i dati dei pixel dell'immagine
    width, height = image.size  # Ottiene la dimensione dell'immagine

    bits = ""
    for i in range(width * height):
        pixel = pixels[i]
        for j in range(3):  # Considera i valori R, G, B
            bits += str(
                pixel[j] & 1
            )  # Estrae il bit meno significativo e lo aggiunge alla stringa di bit
    return bits_to_message(bits)  # Converte la stringa di bit in un messaggio di testo


# Richiede all'utente di inserire il percorso dell'immagine
image_path = input("Inserisci il percorso dell'immagine da cui estrarre il messaggio: ")

# Estrae il messaggio nascosto dall'immagine
hidden_message = extract_message(image_path)
print("Messaggio nascosto:", hidden_message)
