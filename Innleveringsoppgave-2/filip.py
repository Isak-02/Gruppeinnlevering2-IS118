# Min løsning av oppgaven

total_skår = 0

# Erlings beslutning nr. 1

print("BESLUTNING 1 Konflikt mellom Silje og Sivert")
print("1: Erling tar konflikten opp i plenum.")
print("2: Erling tar individuelle samtaler.")

valg1 = input("Skriv 1 eller 2: ")

if valg1 == "1":
    print("Erling tar det opp i plenum.")
    print("Konsekvens: Konflikten blir synlig, men fremdriften øker.")
    total_skår = total_skår + 1 

else:
    print("Erling tar individuelle samtaler.")
    print("Konsekvens: Tilliten øker, men fremdriften blir litt tregere.")

# Erlings beslutning nr. 2

print("BESLUTNING 2 - Konflikt mellom Hamdi og Jabir")
print("1: Erling avventer og håper de løser det selv.")
print("2: Erling tar en beslutning alene.")

valg2 = input("Skriv 1 eller 2: ")

if valg2 == "1":
    print("Erling avventer.")
    print("Konsekvens: De løser konflikten, men det blir klein stemning.")
    total_skår = total_skår - 1
else: 
    print("Erling bestemmer selv.")
    print("Konsekvens: God fremdrift, men Hamdi og Jabir føler seg ikke hørt.")

# Erlings beslutning nr. 3 

print("BESLUTNING 3 - Frafall i motivasjon")
print("1: Erling fokuserer på relasjonsbygging.")
print("2: Erling fokuserer på fremdrift og leveranse.")

valg3 = input("Skriv 1 eller 2: ")

if valg3 == "1":
    print("Erling fokuserer på relasjoner.")
    print("Konsekvens: Bedre samarbeid, men litt lavere fremdrift.")
    total_skår = total_skår + 1
else: 
    print("Erling fokuserer på fremdrift.")
    print("Konsekvens: Prosjektet går fremover, men konfliktene kan øke.")
    total_skår = total_skår - 1

# Konklusjoner

print("KONKLUSJON")

if total_skår > 0: 
    print("Teamet gjenoppretter tillit og går videre til norming-fasen.")
elif total_skår == 0:
    print("Konflikten løses delvis, men relasjonene er fortsatt sårbare.")
else: 
    print("Prosjektet mister samhold og blir forsinket.")
