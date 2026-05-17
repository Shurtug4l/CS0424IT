from funcs import f2d, f3d


def main():
    # Menu per la scelta della figura geometrica
    print("Scegli l'operazione che vuoi effettuare:")
    print("1. Calcola perimetro e area di figure geometriche")
    print("2. Calcola volume di solidi geometrici")

    scelta = int(input("Inserisci la tua scelta (1/2): "))

    if scelta == 1:
        # Menu per la scelta della figura piana
        print(
            "Scegli la figura geometrica di cui vuoi calcolare il perimetro e l'area:"
        )
        print("1. Cerchio")
        print("2. Ellisse")
        print("3. Poligono regolare con n lati")

        figura_piana = int(input("Inserisci la tua scelta (1/2/3): "))

        if figura_piana == 1:
            perimetro, area = f2d.calcola_cerchio()
            print(f"Perimetro del cerchio: {perimetro:.2f}")
            print(f"Area del cerchio: {area:.2f}")
        elif figura_piana == 2:
            perimetro, area = f2d.calcola_ellisse()
            print(f"Perimetro dell'ellisse: {perimetro:.2f}")
            print(f"Area dell'ellisse: {area:.2f}")
        elif figura_piana == 3:
            perimetro, area = f2d.calcola_poligono_regolare()
            print(f"Perimetro del poligono regolare: {perimetro:.2f}")
            print(f"Area del poligono regolare: {area:.2f}")
        else:
            print("Scelta non valida. Riprova.")

    elif scelta == 2:
        # Menu per la scelta del solido geometrico
        print("Scegli il solido geometrico di cui vuoi calcolare il volume:")
        print("1. Sfera")
        print("2. Ellissoide")
        print("3. Cubo")
        print("4. Tetraedro regolare")

        solido = int(input("Inserisci la tua scelta (1/2/3/4): "))

        if solido == 1:
            volume = f3d.calcola_sfera()
            print(f"Volume della sfera: {volume:.2f}")
        elif solido == 2:
            volume = f3d.calcola_ellissoide()
            print(f"Volume dell'ellissoide: {volume:.2f}")
        elif solido == 3:
            volume = f3d.calcola_cubo()
            print(f"Volume del cubo: {volume:.2f}")
        elif solido == 4:
            volume = f3d.calcola_tetraedro_regolare()
            print(f"Volume del tetraedro regolare: {volume:.2f}")
        else:
            print("Scelta non valida. Riprova.")

    else:
        print("Scelta non valida. Riprova.")


if __name__ == "__main__":
    main()
