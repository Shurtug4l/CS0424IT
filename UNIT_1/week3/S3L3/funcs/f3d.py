import numpy as np


def calcola_sfera():
    """
    Funzione per il calcolo del volume di una sfera.
    """
    raggio = float(input("Inserisci il raggio della sfera: "))
    volume = (4 / 3) * np.pi * raggio**3
    return volume


def calcola_ellissoide():
    """
    Funzione per il calcolo del volume di un ellissoide.
    """
    semi_asse_a = float(input("Inserisci il semiasse maggiore dell'ellissoide (a): "))
    semi_asse_b = float(input("Inserisci il semiasse medio dell'ellissoide (b): "))
    semi_asse_c = float(input("Inserisci il semiasse minore dell'ellissoide (c): "))
    volume = (4 / 3) * np.pi * semi_asse_a * semi_asse_b * semi_asse_c
    return volume


def calcola_cubo():
    """
    Funzione per il calcolo del volume di un cubo.
    """
    lato = float(input("Inserisci la lunghezza del lato del cubo: "))
    volume = lato**3
    return volume


def calcola_tetraedro_regolare():
    """
    Funzione per il calcolo del volume di un tetraedro regolare.
    """
    lato = float(input("Inserisci la lunghezza del lato del tetraedro regolare: "))
    volume = (lato**3) / (6 * np.sqrt(2))
    return volume
