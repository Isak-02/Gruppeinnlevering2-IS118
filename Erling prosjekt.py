
print("Velkommen — du spiller som Erling, prosjektleder for den nye digitale medborgerportalen.")
print("Situasjonen: Teamet er i storming-fasen. Du må ta tre viktige beslutninger.")
print("")

# --- Beslutning 1
print("BESLUTNING 1: Hvordan håndtere konflikten mellom Silje (design) og Sivert (teknologi)?")
print("  a) Ta det opp i plenum (åpen diskusjon)")
print("  b) Ta individuelle samtaler (privat)")
first_choice = input("Velg a eller b: ")
first_choice = first_choice.lower()
if first_choice == "":
    print("Ugyldig input - standard velges (a).")
    first_choice = "a"
else:
    first_choice = first_choice[0]
    if first_choice != "a" and first_choice != "b":
        print("Ugyldig valg - standard velges (a).")
        first_choice = "a"

if first_choice == "a":
    approach_conflict = "plenum"
    print("Du valgte plenum. Fordeler: åpenhet. Risiko: kan eskalere.")
else:
    approach_conflict = "individuelt"
    print("Du valgte individuelle samtaler. Fordeler: demper temperaturen. Risiko: noen kan føle seg lite hørt.")

print("")

# --- Beslutning 2
print("BESLUTNING 2: Hvordan håndtere uenigheten om digitale folkemøter mellom Hamdi og Jabir?")
print("  a) Avvente og la dem finne en løsning selv")
print("  b) Ta en beslutning selv som leder (klare rammer)")
second_choice = input("Velg a eller b: ")
second_choice = second_choice.lower()
if second_choice == "":
    print("Ugyldig input - standard velges (a).")
    second_choice = "a"
else:
    second_choice = second_choice[0]
    if second_choice != "a" and second_choice != "b":
        print("Ugyldig valg - standard velges (a).")
        second_choice = "a"

if second_choice == "a":
    resolution_civic = "avvente"
    print("Du valgte å avvente. Fordeler: partene kan vokse ved egen dialog. Risiko: ujevn maktbalanse kan gi misnøye.")
else:
    resolution_civic = "lederbeslutning"
    print("Du valgte lederbeslutning. Fordeler: tydelig retning og fremdrift. Risiko: noen kan føle seg overkjørt.")

print("")

# --- Beslutning 3
print("BESLUTNING 3: Hvordan styrke motivasjonen i teamet?")
print("  a) Prioritere relasjonsbygging (teambuilding og samtaler)")
print("  b) Prioritere fremdrift (fokus på leveranser)")
third_choice = input("Velg a eller b: ")
third_choice = third_choice.lower()
if third_choice == "":
    print("Ugyldig input - standard velges (a).")
    third_choice = "a"
else:
    third_choice = third_choice[0]
    if third_choice != "a" and third_choice != "b":
        print("Ugyldig valg - standard velges (a).")
        third_choice = "a"

if third_choice == "a":
    motivation = "relasjoner"
    print("Du valgte relasjonsbygging. Fordeler: økt tillit. Risiko: midlertidig lavere fremdrift.")
else:
    motivation = "fremdrift"
    print("Du valgte fremdrift. Fordeler: synlig fremdrift. Risiko: uadressert konflikt kan eskalere.")

print("")
print("---")
print("Sammenfatning av valg:")
print(" Konflikthåndtering Silje/Sivert: " + approach_conflict)
print(" Hamdi/Jabir-løsning: " + resolution_civic)
print(" Fokus for motivasjon: " + motivation)
print("")

# --- Bestemme endepunkt kun med if / elif / else
if approach_conflict == "plenum" and resolution_civic == "avvente" and motivation == "relasjoner":
    outcome = 1
elif approach_conflict == "individuelt" and resolution_civic == "lederbeslutning" and motivation == "fremdrift":
    outcome = 3
else:
    outcome = 2

print("---")
print("RESULTAT — ENDEPUNKT:")
if outcome == 1:
    print("1) Teamet gjenoppretter tillit og går videre til norming-fasen.")
    print("   Forklaring: Åpenhet + dialog + relasjonsbygging skapte felles forståelse.")
elif outcome == 2:
    print("2) Konflikten løses delvis, men relasjonsbåndene er fortsatt sårbare.")
    print("   Forklaring: Noen riktige valg, men spenninger gjenstår.")
else:
    print("3) Prosjektet mister samhold og blir forsinket.")
    print("   Forklaring: Fokus på fremdrift ga resultater, men underliggende konflikter svekket samarbeid.")

print("")
print("Takk for at du spilte. Lykke til videre!")
print("")