#include <stdio.h>

void menu();
void moltiplica();
void dividi();
void ins_string();

int main() 
{
    char scelta = '\0';
    menu();
    scanf(" %c", &scelta);

    switch (scelta)
    {
        case 'A':
        case 'a':
            moltiplica();
            break;
        case 'B':
        case 'b':
            dividi();
            break;
        case 'C':
        case 'c':
            ins_string();
            break;
        default:
            printf("Scelta non valida.\n");
            break;
    }

    return 0;
}

void menu()
{
    printf("Benvenuto, sono un assistente digitale, posso aiutarti a sbrigare alcuni compiti\n");
    printf("Come posso aiutarti?\n");
    printf("A >> Moltiplicare due numeri\n");
    printf("B >> Dividere due numeri\n");
    printf("C >> Inserire una stringa\n");
}

void moltiplica()
{
    int a, b;
    printf("Inserisci i due numeri da moltiplicare: ");
    if (scanf("%d %d", &a, &b) != 2) {
        printf("Errore: Input non valido.\n");
        return;
    }

    int prodotto = a * b;
    printf("Il prodotto tra %d e %d è: %d\n", a, b, prodotto);
}

void dividi()
{
    int a, b;
    printf("Inserisci il numeratore: ");
    if (scanf("%d", &a) != 1) {
        printf("Errore: Input non valido.\n");
        return;
    }
    printf("Inserisci il denominatore: ");
    if (scanf("%d", &b) != 1) {
        printf("Errore: Input non valido.\n");
        return;
    }
    if (b == 0) {
        printf("Errore: Divisione per zero.\n");
        return;
    }

    float divisione = (float)a / b;
    printf("La divisione tra %d e %d è: %.2f\n", a, b, divisione);
}

void ins_string()
{
    char stringa[10];
    printf("Inserisci la stringa (max 9 caratteri): ");
    scanf("%9s", stringa);
    printf("Hai inserito: %s\n", stringa);
}
