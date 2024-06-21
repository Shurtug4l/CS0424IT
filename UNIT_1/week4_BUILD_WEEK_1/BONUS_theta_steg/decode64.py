import base64

# Lista dei file base64 in ordine
file_parts = [ 
        "flag-aa.txt",
        "flag-ab.txt",
        "flag-ac.txt",
        "flag-ad.txt",
        "flag-aef.txt",
        "flag-ag.txt",
        "flag-ah.txt"
        ]

# Lettura dei file e concatenazione dei contenuti
base64_content = ""
for file_name in file_parts:
    with open(file_name, "r") as file:
        base64_content += file.read()

# Decodifica del contenuto base64
decoded_content = base64.b64decode(base64_content)

# Salvataggio del contenuto decodificato in un file
with open("decoded_flag_abcd", "wb") as decoded_file:
    decoded_file.write(decoded_content)

print("File decodificato salvato come 'decoded_flag'")
