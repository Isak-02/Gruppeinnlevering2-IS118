print("Velkommen — du spiller som Erling, prosjektleder for den nye digitale medborgerportalen.")
print("Situasjonen: Teamet er i storming-fasen. Du må ta tre viktige beslutninger.")


# --- Beslutning 1 ---
def konflikt1():
    print("\nKonflikt 1")
    print("Hvordan håndtere konflikten mellom Silje og Sivert?")
    print("1. Erling kan velge å ta dette opp i plenum sammen med resten av teamet.")
    print("2. Erling kan ta individuelle samtaler med Silje og Sivert. .")

    while True:
        valg = input("Velg 1 eller 2: ")

        if valg == "1":
            print("\nKonsekvens: Erling tar det opp i plenum. Konflikten blir synlig, men fremdriften øker..")
            print("Poeng: 3\n")
            return 3

        elif valg == "2":
            print("\nKonsekvens: Erling tar individuelle samtaler. Tilliten øker, men fremdriften går litt tregere.")
            print("Poeng: 2\n")
            return 2


        else:
            print("Ugyldig valg, prøv igjen.")

# --- Beslutning 2 ---
def konflikt2():
    print("\nKonflikt 2")
    print("Hvordan håndtere konflikten mellom Hambi og Jabir?")
    print("1. Erling avventer og håper at partene finner en løsning selv.")
    print("2. Erling kan ta en beslutning uten å inkludere teamet.")

    while True:
        valg = input("Velg 1 eller 2: ")

        if valg == "1":
            print("\nKonsekvens: Hamdi og Jabir løser konflikten, men det er klein stemning mellom partene.")
            print("Poeng: 3\n")
            return 3

        elif valg == "2":
            print("\nKonsekvens: Hamdi og Jabir føler seg ikke hørt, men prosjektet har god fremdrift..")
            print("Poeng: -2\n")
            return -2
        

        else:
            print("Ugyldig valg, prøv igjen.")

# --- Beslutning 3 ---
def konflikt3():
    print("\nKonflikt 3")
    print("Hvordan bevare motivasjonen i teamet som helhet?")
    print("1. Erling fokuserer på relasjonsbygging og teamfokus.")
    print("2. Erling fokuserer på fremdrift og samhold..")

    while True:
        valg = input("Velg 1 eller 2: ")

        if valg == "1":
            print("\nKonsekvens: Teamet får bedre samarbeid og klima, men risiko for litt lavere fremdrift.")
            print("Poeng: 3\n") 
            return 3

        elif valg == "2":
            print("\nKonsekvens: Prosjektet kommer videre men teamet risikerer langvarige samarbeidsproblemer.")
            print("Poeng: 1\n") 
            return 1


        else:
            print("Ugyldig valg, prøv igjen.")


def main():
    

    total_poeng = 0

    total_poeng += konflikt1()
    total_poeng += konflikt2()
    total_poeng += konflikt3()

    print("\nRESULTAT")
    print("Totale poeng:", total_poeng)

    if total_poeng >= 7:
        print("\nRESULTAT: Teamet fungerer veldig godt!")
        print("Forklaring: Valgene gjennoprettet tillit og styrket motivasjon. Prosjektet kommer seg videre til norming fasen.")
    elif total_poeng >= 3:
        print("\nRESULTAT: Løses delvis")
        print("Forklaring: Konflikten løses delvis, men relasjonene er fortsatt sårbare.")
    else:
        print("\nRESULTAT: Prosjektet mister samhold og blir forsinket.")
        print("Forklaring: Valgene fører til at teamet sliter med samarbeid og prosjektet blir forsinket.")


if __name__ == "__main__":
    main()
    
    