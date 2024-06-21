from PIL import Image


# Funzione per convertire un messaggio di testo in una stringa di bit
def message_to_bits(message):
    bits = []
    for char in message:
        bits.append(
            bin(ord(char))[2:].zfill(8)
        )  # Converte ogni carattere in una stringa di 8 bit
    return "".join(bits)  # Unisce tutte le stringhe di bit in una singola stringa


# Funzione per incorporare un messaggio nascosto in un'immagine
def embed_message(image_path, output_path, message):
    image = Image.open(image_path)  # Carica l'immagine
    encoded_image = image.copy()  # Crea una copia dell'immagine
    width, height = image.size  # Ottiene la dimensione dell'immagine
    pixels = list(image.getdata())  # Ottiene i dati dei pixel dell'immagine

    message_bits = message_to_bits(message)  # Converte il messaggio in bit
    message_bits += (
        "0" * 8
    )  # Aggiunge un carattere nullo per indicare la fine del messaggio
    bit_index = 0  # Indice per tenere traccia della posizione nel messaggio di bit

    for i in range(width * height):
        if bit_index < len(message_bits):
            pixel = list(
                pixels[i]
            )  # Converte il pixel in una lista per modificare i valori RGB
            for j in range(3):  # Modifica i valori R, G, B
                if bit_index < len(message_bits):
                    pixel[j] = pixel[j] & ~1 | int(
                        message_bits[bit_index]
                    )  # Modifica il bit meno significativo
                    bit_index += 1  # Passa al bit successivo del messaggio
            pixels[i] = tuple(
                pixel
            )  # Riporta il pixel modificato nella lista dei pixel
        else:
            break

    encoded_image.putdata(pixels)  # Aggiorna i dati dei pixel dell'immagine
    encoded_image.save(output_path)  # Salva l'immagine modificata


# Richiede all'utente di inserire il percorso dell'immagine e il messaggio
input_image_path = input("Inserisci il percorso dell'immagine di input: ")
output_image_path = input("Inserisci il percorso dell'immagine di output: ")
message = input("Inserisci il messaggio da nascondere: ")

# Esegue la funzione di incorporamento
embed_message(input_image_path, output_image_path, message)
