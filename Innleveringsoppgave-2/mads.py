# Det brukes noen enkle variabler for å lagre tillit og fremdrift poeng i teamet.
# I dette tilfellet er "tillit" en variabel, og "0" er en verdi.
# Senere i koden vil verdien av variabelen bli endret (1+ eller 1-) basert på hva brukeren gir som input (1 eller 2).
# = er tilordningsoperatoren. Den setter verdien på høyre side til variabelen på venstre side.
# 0 er et heltall (integer) som starter verdien.
# Dette tallet kunne vært annerledes.
# I dette tilfellet er det 0 fordi teamet starter med null poeng.
# Det er brukeren som avgjør poengene basert på valgene som blir gjort i terminalen.

tillit = 0      
fremdrift = 0   

# print() er en innebygd funksjon som skriver ut tekst til terminalen.
# Tekst mellom anførselstegn ("") kalles en streng (string).
# Uten anførselstegn vil man få en syntax feil. "SyntaxError: invalid syntax."

# \n betyr "ny linje". det lager et linjeskift. Dette blir brukt for å skape pusterom i teminalen for leseren.
# Her blir det printet "-------" og "DEL 1" Slik at leseren enkelt kan navigere seg til ulike deler av historien.

print("\n---------------------------- INTRO ----------------------------")

print("\nVelkommen til historien om Erling og medborgerportalen.")
print("\nI dag skal du sette deg inn i rollen til Erling, og ta noen\nviktige valg som vil avgjøre fremdriften og tilliten til teamet.")
print("\nTeamet er i storming-fasen, og Erling må ta noen viktige valg.")

# ------------------ BESLUTNING 1 ------------------
# Konflikten mellom Silje og Sivert

print("\n---------------------------- DEL 1 ----------------------------\n")

print("BESLUTNING 1: Konflikten mellom Silje og Sivert.\n")
print("1) Erling tar konflikten opp i plenum foran hele teamet.")
print("2) Erling tar individuelle samtaler med Silje og Sivert.")

# input() er en funksjon som venter på at brukeren skriver noe og trykker Enter.
# Den returnerer det brukeren skrev som en streng.
# Svaret blir lagret i variabelen valg1.
valg1 = input("\nTa valget for Erling og skriv: 1 eller 2: ")

# while er en løkke som gjentar kode så lenge betingelsen er sann.
# != betyr "ikke lik" - så lenge valg1 ikke er "1" og ikke er "2", fortsetter løkken.
while valg1 != "1" and valg1 != "2":
    # and er en logisk operator som krever at begge sider er sanne.
    print("Ugyldig valg! Skriv 1 eller 2:")
    valg1 = input("Ta valget for Erling og skriv: 1 eller 2: ")

# if starter en betingelsesblokk. koden under kjører hvis betingelsen er sann.
# For eksempel hvis(if) bruker skriver 1 (og enter), så vil X blir printet (print("X")). Hvis bruker skriver 2 (og enter), så vil Y blir printet (print("Y")).
# == er sammenligningsoperatoren som sjekker om to verdier er like.
# For eksempel hvis valg1 er lik 1, så vil X blir printet (print("X")). Hvis valg1 er lik 2, så vil Y blir printet (print("Y")).
if valg1 == "1":
    print("\nErling tar det opp i plenum. Konflikten blir synlig, men de får ryddet opp noe.")
    # += er en forkortelse for "legg til og sett".
    # Fremdrift += 1 er det samme som fremdrift = fremdrift + 1. Fremdrift får ett "poeng" her.
    fremdrift += 1      
    # -= er en forkortelse for "trekk fra og sett"
    # Tillit -= 1 er det samme som tillit = tillit - 1. Tillit får ett "minuspoeng" her.
    tillit -= 1         
# elif er en forkortelse for "else if" - sjekker en ny betingelse hvis den forrige var usann
# Enkel forklaring: Hvis X blir skrevet, så skal Y bli printet, Ellers hvis Z blir skrevet, så skal A blir printet.
elif valg1 == "2":
    print("\nErling tar individuelle samtaler. Tilliten mellom partene øker, men det tar litt tid.")
    tillit += 1
    fremdrift -= 1

print("\n---------------------------- DEL 2 ----------------------------\n")

# ------------------ BESLUTNING 2 ------------------
# Konflikten mellom Hamdi (kultur) og Jabir (brukerrepresentant)

print("BESLUTNING 2: Uenighet mellom Hamdi og Jabir om digitale folkemøter.\n")
print("1) Erling avventer og håper at de løser konflikten selv.")
print("2) Erling tar en beslutning selv uten å involvere teamet.\n")

valg2 = input("Ta valget for Erling og skriv: 1 eller 2: ")

# Validering av input - brukeren må skrive 1 eller 2
while valg2 != "1" and valg2 != "2":
    print("Ugyldig valg! Skriv 1 eller 2:")
    valg2 = input("Ta valget for Erling og skriv: 1 eller 2: ")

if valg2 == "1":
    print("\nHamdi og Jabir prøver å løse det selv. De finner en løsning, men det er litt klein stemning.")
    tillit += 1         
elif valg2 == "2":
    print("\nErling bestemmer løsningen selv. Fremdriften blir tydelig, men Hamdi og Jabir føler seg lite hørt.")
    fremdrift += 1
    tillit -= 1

print("\n---------------------------- DEL 3 ----------------------------\n")

# ------------------ BESLUTNING 3 ------------------
# Frafall i motivasjon i hele teamet

print("BESLUTNING 3: Motivasjonen i teamet faller.\n")
print("1) Erling fokuserer på relasjonsbygging og teambygging.")
print("2) Erling fokuserer på fremdrift og leveranser.\n")

valg3 = input("Ta valget for Erling og skriv: 1 eller 2: ")

# Validering av input - brukeren må skrive 1 eller 2
while valg3 != "1" and valg3 != "2":
    print("Ugyldig valg! Skriv 1 eller 2:")
    valg3 = input("Ta valget for Erling og skriv: 1 eller 2: ")

print("\n--------------------------- RESULTAT---------------------------\n")

if valg3 == "1":
    print("Erling setter av tid til relasjonsbygging. Teamet får bedre trygghet, men mister litt tid.")
    tillit += 2
    fremdrift -= 1
elif valg3 == "2":
    print("Erling presser på for fremdrift. De leverer mer, men teamet er fortsatt urolig under overflaten.\n")
    fremdrift += 2
    tillit -= 1

# ------------------ SLUTTUTFALL ------------------
# Det lages tre mulige ender basert på tillit og fremdrift.

# f"" er en f-streng (f-string) som lar oss sette inn variabler direkte i teksten
# {tillit} og {fremdrift} erstattes med verdiene i variablene
print(f"(Status til slutt: tillit = {tillit}, fremdrift = {fremdrift})\n")

# >= betyr "større enn eller lik" - sjekker om verdien er større eller lik tallet
if tillit >= 2 and fremdrift >= 1:
    print("UTFALL 1: Teamet gjenoppretter tillit og går videre til norming-fasen.\n")
    print("Konfliktene er tatt på alvor, relasjonene er styrket, og teamet jobber samlet mot målene.\n")
elif tillit >= 0 and fremdrift >= 1:
    print("UTFALL 2: Konfliktene er delvis løst, men relasjonene er fortsatt sårbare.\n")
    print("Prosjektet går fremover, men det skal lite til før det oppstår nye spenninger.\n")
# else kjører hvis ingen av de forrige betingelsene var sanne
else:
    print("UTFALL 3: Prosjektet mister samhold og blir forsinket.\n")
    print("Fremdrift og tillit ble ikke godt nok ivaretatt, og teamet sliter med å komme videre.\n")
