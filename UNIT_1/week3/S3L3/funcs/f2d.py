import numpy as np


def calcola_cerchio():
    """
    Funzione per il calcolo del perimetro/area di circonferenza/cerchio.
    """
    raggio = float(input("Inserisci il raggio del cerchio: "))
    perimetro = 2 * np.pi * raggio
    area = np.pi * raggio**2
    return perimetro, area


def calcola_ellisse():
    """
    Funzione per il calcolo del perimetro/area di un'ellisse.
    """
    semiasse_maggiore = float(input("Inserisci il semiasse maggiore dell'ellisse: "))
    semiasse_minore = float(input("Inserisci il semiasse minore dell'ellisse: "))
    perimetro = np.pi * (
        3 * (semiasse_maggiore + semiasse_minore)
        - np.sqrt(
            (3 * semiasse_maggiore + semiasse_minore)
            * (semiasse_maggiore + 3 * semiasse_minore)
        )
    )
    area = np.pi * semiasse_maggiore * semiasse_minore
    return perimetro, area


def calcola_poligono_regolare():
    """
    Funzione per il calcolo del perimetro/area di un poligono regolare qualunque.
    """
    n_lati = int(input("Inserisci il numero di lati del poligono regolare: "))
    lunghezza_lato = float(
        input("Inserisci la lunghezza di un lato del poligono regolare: ")
    )
    perimetro = n_lati * lunghezza_lato
    apotema = lunghezza_lato / (2 * np.tan(np.pi / n_lati))
    area = (perimetro * apotema) / 2
    return perimetro, area
