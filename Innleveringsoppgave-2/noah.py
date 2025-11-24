# Interaktiv historie - IS-118 Innleveringsoppgave 2
# Tema: Prosjektleder Erling og teamkonflikter
# 3 beslutningspunkter med 2 valg hver

def hent_valg(sporsmal):
    while True:
        valg = input(sporsmal + " (A/B): ").strip().upper()
        if valg in ["A", "B"]:
            return valg
        else:
            print("Ugyldig valg. Skriv A eller B.")


print("=== INTERAKTIV HISTORIE: ERLING SOM PROSJEKTLEDER ===\n")
print("Du er Erling, prosjektleder for en ny digital medborgerportal.")
print("Prosjektet har gått inn i storming-fasen, og konflikter preger teamet.\n")

# BESLUTNING 1
print("Beslutning 1: Konflikten mellom Silje og Sivert eskalerer.")
print("A: Ta konflikten opp i plenum for å skape åpenhet.")
print("B: Ta individuelle samtaler med hver av dem.")

valg1 = hent_valg("Hva velger du?")

if valg1 == "A":
    print("\nDiskusjonen i plenum blir intens, men alle perspektiver kommer frem.")
    konsekvens1 = "åpen konflikt"
else:
    print("\nSamtalene roer situasjonen noe, men spenningen ligger fortsatt i luften.")
    konsekvens1 = "dempe konflikt"

# BESLUTNING 2
print("\nBeslutning 2: Uenighet mellom Hamdi og Jabir om digitale folkemøter.")
print("A: Kalle inn til felles møte for dialog.")
print("B: Avvente og håpe at de løser det selv.")

valg2 = hent_valg("Hva velger du?")

if valg2 == "A":
    print("\nMøtet fører til bedre forståelse, men krever tid og energi.")
    konsekvens2 = "dialog"
else:
    print("\nUenigheten fortsetter å ulme i bakgrunnen.")
    konsekvens2 = "unngåelse"

# BESLUTNING 3
print("\nBeslutning 3: Teamets motivasjon synker.")
print("A: Prioritere relasjonsbygging og sosiale tiltak.")
print("B: Fokusere kun på leveranser og fremdrift.")

valg3 = hent_valg("Hva velger du?")

if valg3 == "A":
    print("\nTeamet opplever økt samhold og trygghet.")
    konsekvens3 = "fellesskap"
else:
    print("\nResultatfokus gir fremdrift, men relasjonene svekkes.")
    konsekvens3 = "press"

# AVSLUTNING – UTFALL
print("\n=== SLUTTRESULTAT ===")

if konsekvens1 == "dempe konflikt" and konsekvens2 == "dialog" and konsekvens3 == "fellesskap":
    print("Teamet gjenoppretter tillit og beveger seg inn i norming-fasen.")
    print("Samarbeidet styrkes, og prosjektet når milepælene sine.")
elif konsekvens3 == "press" and konsekvens2 == "unngåelse":
    print("Konfliktene forblir uløste og relasjonene svekkes.")
    print("Prosjektet blir forsinket og mister samhold.")
else:
    print("Noen konflikter er håndtert, men relasjonene er fortsatt sårbare.")
    print("Prosjektet går videre, men krever fortsatt tett ledelse.")