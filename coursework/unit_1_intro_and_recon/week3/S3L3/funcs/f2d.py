import numpy as np


def calcola_cerchio():
    """
    Funzione per il calcolo del perimetro/area di circonferenza/cerchio.
    """
    raggio = np.abs(float(input("Inserisci il raggio del cerchio: ")))
    perimetro = 2 * np.pi * raggio
    area = np.pi * raggio**2
    return perimetro, area


def calcola_ellisse():
    """
    Funzione per il calcolo del perimetro/area di un'ellisse.
    """
    semiasse_maggiore = np.abs(
        float(input("Inserisci il primo semiasse dell'ellisse: "))
    )
    semiasse_minore = np.abs(
        float(input("Inserisci il secondo semiasse dell'ellisse: "))
    )
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
    n_lati = np.abs(int(input("Inserisci il numero di lati del poligono regolare: ")))
    lunghezza_lato = np.abs(
        float(input("Inserisci la lunghezza di un lato del poligono regolare: "))
    )
    perimetro = n_lati * lunghezza_lato
    apotema = lunghezza_lato / (2 * np.tan(np.pi / n_lati))
    area = (perimetro * apotema) / 2
    return perimetro, area
