# Dette er en kommentar - alt etter # på samme linje blir ignorert av Python

# Vi bruker noen enkle variabler for å lagre hvordan det går i teamet.
# En variabel er en navngitt plass i minnet hvor vi kan lagre verdier
tillit = 0      # hvor god tillit og relasjoner i teamet
# = er tilordningsoperatoren - den setter verdien på høyre side til variabelen på venstre side
# 0 er et heltall (integer) som starter verdien
fremdrift = 0   # hvor god fremdrift i prosjektet

# print() er en innebygd funksjon som skriver ut tekst til skjermen
# Tekst mellom anførselstegn ("") kalles en streng (string)
# \n betyr "ny linje" - det lager et linjeskift
print("Velkommen til historien om Erling og medborgerportalen.\n")
print("Teamet er i storming-fasen, og Erling må ta noen viktige valg.\n")







# ------------------ BESLUTNING 1 ------------------
# Konflikten mellom Silje (UX) og Sivert (IT)

print("BESLUTNING 1: Konflikten mellom Silje og Sivert.")
print("1) Erling tar konflikten opp i plenum foran hele teamet.")
print("2) Erling tar individuelle samtaler med Silje og Sivert.\n")

# input() er en funksjon som venter på at brukeren skriver noe og trykker Enter
# Den returnerer det brukeren skrev som en streng
# Vi lagrer svaret i variabelen valg1
valg1 = input("Skriv 1 eller 2: ")

# while er en løkke som gjentar kode så lenge betingelsen er sann
# != betyr "ikke lik" - så lenge valg1 ikke er "1" og ikke er "2", fortsetter løkken
while valg1 != "1" and valg1 != "2":
    # and er en logisk operator som krever at begge sider er sanne
    print("Ugyldig valg! Du må skrive 1 eller 2.")
    valg1 = input("Skriv 1 eller 2: ")

# if starter en betingelsesblokk - koden under kjører hvis betingelsen er sann
# == er sammenligningsoperatoren som sjekker om to verdier er like
if valg1 == "1":
    print("\nErling tar det opp i plenum. Konflikten blir synlig, men de får ryddet opp noe.")
    # += er en forkortelse for "legg til og sett" - fremdrift += 1 er det samme som fremdrift = fremdrift + 1
    fremdrift += 1      # bedre fremdrift
    # -= er en forkortelse for "trekk fra og sett" - tillit -= 1 er det samme som tillit = tillit - 1
    tillit -= 1         # noen føler seg kanskje litt angrepet
# elif er en forkortelse for "else if" - sjekker en ny betingelse hvis den forrige var usann
elif valg1 == "2":
    print("\nErling tar individuelle samtaler. Tilliten mellom partene øker, men det tar litt tid.")
    tillit += 1
    fremdrift -= 1

print("\n--- Videre i historien ---\n")







# ------------------ BESLUTNING 2 ------------------
# Konflikten mellom Hamdi (kultur) og Jabir (brukerrepresentant)

print("BESLUTNING 2: Uenighet mellom Hamdi og Jabir om digitale folkemøter.")
print("1) Erling avventer og håper at de løser konflikten selv.")
print("2) Erling tar en beslutning selv uten å involvere teamet.\n")

valg2 = input("Skriv 1 eller 2: ")

# Validering av input - brukeren må skrive 1 eller 2
while valg2 != "1" and valg2 != "2":
    print("Ugyldig valg! Du må skrive 1 eller 2.")
    valg2 = input("Skriv 1 eller 2: ")

if valg2 == "1":
    print("\nHamdi og Jabir prøver å løse det selv. De finner en løsning, men det er litt klein stemning.")
    tillit += 1         # de har samarbeidet, men det sitter litt i veggene
elif valg2 == "2":
    print("\nErling bestemmer løsningen selv. Fremdriften blir tydelig, men Hamdi og Jabir føler seg lite hørt.")
    fremdrift += 1
    tillit -= 1

print("\n--- Siste fase i historien ---\n")






# ------------------ BESLUTNING 3 ------------------
# Frafall i motivasjon i hele teamet

print("BESLUTNING 3: Motivasjonen i teamet faller.")
print("1) Erling fokuserer på relasjonsbygging og teambygging.")
print("2) Erling fokuserer på fremdrift og leveranser.\n")

valg3 = input("Skriv 1 eller 2: ")

# Validering av input - brukeren må skrive 1 eller 2
while valg3 != "1" and valg3 != "2":
    print("Ugyldig valg! Du må skrive 1 eller 2.")
    valg3 = input("Skriv 1 eller 2: ")

if valg3 == "1":
    print("\nErling setter av tid til relasjonsbygging. Teamet får bedre trygghet, men mister litt tid.")
    tillit += 2
    fremdrift -= 1
elif valg3 == "2":
    print("\nErling presser på for fremdrift. De leverer mer, men teamet er fortsatt urolig under overflaten.")
    fremdrift += 2
    tillit -= 1

print("\n--- SLUTT PÅ HISTORIEN ---\n")





# ------------------ SLUTTUTFALL ------------------
# Vi lager tre mulige ender basert på tillit og fremdrift.

# f"" er en f-streng (f-string) som lar oss sette inn variabler direkte i teksten
# {tillit} og {fremdrift} erstattes med verdiene i variablene
print(f"(Status til slutt: tillit = {tillit}, fremdrift = {fremdrift})\n")

# >= betyr "større enn eller lik" - sjekker om verdien er større eller lik tallet
if tillit >= 2 and fremdrift >= 1:
    print("UTFALL 1: Teamet gjenoppretter tillit og går videre til norming-fasen.")
    print("Konfliktene er tatt på alvor, relasjonene er styrket, og teamet jobber samlet mot målene.")
elif tillit >= 0 and fremdrift >= 1:
    print("UTFALL 2: Konfliktene er delvis løst, men relasjonene er fortsatt sårbare.")
    print("Prosjektet går fremover, men det skal lite til før det oppstår nye spenninger.")
# else kjører hvis ingen av de forrige betingelsene var sanne
else:
    print("UTFALL 3: Prosjektet mister samhold og blir forsinket.")
    print("Fremdrift og tillit ble ikke godt nok ivaretatt, og teamet sliter med å komme videre.")
