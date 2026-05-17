import numpy as np


def calcola_sfera():
    """
    Funzione per il calcolo del volume di una sfera.
    """
    raggio = np.abs(float(input("Inserisci il raggio della sfera: ")))
    volume = (4 / 3) * np.pi * raggio**3
    return volume


def calcola_ellissoide():
    """
    Funzione per il calcolo del volume di un ellissoide.
    """
    semi_asse_a = np.abs(
        float(input("Inserisci il primo semiasse dell'ellissoide (a): "))
    )
    semi_asse_b = np.abs(
        float(input("Inserisci il secondo semiasse dell'ellissoide (b): "))
    )
    semi_asse_c = np.abs(
        float(input("Inserisci il terzo semiasse dell'ellissoide (c): "))
    )
    volume = (4 / 3) * np.pi * semi_asse_a * semi_asse_b * semi_asse_c
    return volume


def calcola_cubo():
    """
    Funzione per il calcolo del volume di un cubo.
    """
    lato = np.abs(float(input("Inserisci la lunghezza del lato del cubo: ")))
    volume = lato**3
    return volume


def calcola_tetraedro_regolare():
    """
    Funzione per il calcolo del volume di un tetraedro regolare.
    """
    lato = np.abs(
        float(input("Inserisci la lunghezza del lato del tetraedro regolare: "))
    )
    volume = (lato**3) / (6 * np.sqrt(2))
    return volume
