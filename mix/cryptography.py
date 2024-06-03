# istruzioni per la prova
# su linux: pip install cryptography
# su mac: brew install python-cryptography
# openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048
# openssl rsa -pubout -in private_key.pem -out public_key.pem

import base64

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

# Carica la chiave pubblica
with open("public_key.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(), backend=default_backend()
    )

# Carica la chiave privata
with open("private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(), password=None, backend=default_backend()
    )

# Messaggio da criptare
message = b"Ciao, Epicode spacca!"

# Criptazione con la chiave pubblica
encrypted = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)

# Decriptazione con la chiave privata
decrypted = private_key.decrypt(
    encrypted,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)

print("Messaggio originale:", message.decode())
print("Messaggio decriptato:", decrypted.decode())

# Criptazione con la chiave privata (firmatura)
signed = private_key.sign(
    message,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256(),
)

# Verifica con la chiave pubblica
try:
    encrypted_b64 = base64.b64encode(signed).decode("utf-8")
    public_key.verify(
        signed,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256(),
    )
    print(
        "Rappresentazione base64 del messaggio criptato dalla chiave privata:\n",
        encrypted_b64,
    )
    print("Messaggio originale da confrontare:", message.decode())
    print("La firma è valida.")
except Exception as e:
    print("La firma non è valida.", str(e))
