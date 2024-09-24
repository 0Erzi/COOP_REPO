from back_end import *


def printMeny():
    print("\n------------------- Kalkulator -------------------")
    print("| 1. Legg sammen (pluss)                         |")
    print("| 2. Trekk fra   (minus)                         |")
    print("| 3. Gange                                       |")
    print("| 4. Dele                                        |")
    print("| 5. Avslutt                                     |")
    print("--------------------------------------------------")
    menyvalg = input("Velg operasjon fra menyen (1-5): ")
    utfoerMenyvalg(menyvalg)


def utfoerMenyvalg(valgtTall):
    if valgtTall == "1":
        leggSammen()
    elif valgtTall == "2":
        trekkFra()
    elif valgtTall == "3":
        gange()
    elif valgtTall == "4":
        dele()
    elif valgtTall == "5":
        avslutt()
    else:
        print("*** Ugyldig valg. Velg et tall mellom 1-5. ***")
        printMeny()

    pause_og_fortsett()


def leggSammen():
    num1, num2 = hentTall("pluss")
    print(f"Resultat: {num1} + {num2} = {num1 + num2}")


def trekkFra():
    num1, num2 = hentTall("minus")
    print(f"Resultat: {num1} - {num2} = {num1 - num2}")


def gange():
    num1, num2 = hentTall("gange")
    print(f"Resultat: {num1} * {num2} = {num1 * num2}")


def dele():
    num1, num2 = hentTall("dele")
    try:
        resultat = num1 / num2
        print(f"Resultat: {num1} / {num2} = {resultat}")
    except ZeroDivisionError:
        print("*** Feil: Kan ikke dele med null. Prøv igjen. ***")


def hentTall(operasjon):
    while True:
        try:
            num1 = float(input(f"Oppgi første tall for å {operasjon}: "))
            num2 = float(input(f"Oppgi andre tall for å {operasjon}: "))
            return num1, num2
        except ValueError:
            print("*** Ugyldig input. Skriv inn gyldige tall. ***")


def pause_og_fortsett():
    input("\n-- Trykk en tast for å fortsette --")
    printMeny()


def avslutt():
    bekreftelse = input("Er du sikker på at du vil avslutte? (J/N): ")
    if bekreftelse.lower() == "j":
        print("Avslutter kalkulatoren. Ha en fin dag!")
        exit()
    else:
        printMeny()


printMeny()
