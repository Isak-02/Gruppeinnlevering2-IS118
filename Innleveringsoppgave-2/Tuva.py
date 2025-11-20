# IS-118 Del 2 - Interaktiv historie med fremdrift

# Startverdier
fremdrift = 50  
tillit = 50      

print("\nProsjektet har nådd storming-fasen. Erling må ta viktige valg.")
print(f"Status ved start: Fremdrift = {fremdrift}, Tillit = {tillit}\n")

input("Trykk enter for å fortsette...\n")
print("--------------------------------------------------\n")

# --- Beslutning 1: Konflikten mellom Silje og Sivert ---

print("Beslutning 1: Konflikten mellom Silje og Sivert")
print("---------------------------------------------------\n")
print("Diskusjonene mellom Silje og Sivert blir stadig mer emosjonelle, og Erling må gripe inn.\n")
print("Beslutning 1: Hvilket valg bør Erling ta for å gripe inn i situasjonen?")

print("1: Ta det opp i plenum for å skape åpenhet")
print("2: Ha individuelle samtaler for å dempe temperaturen")
choice1 = input("Ditt valg (1/2): ")

if choice1 == "1":
    tillit -= 10
    fremdrift += 10
    print(f"\nDu tar det opp i plenum. Konflikten blir synlig, men fremdriften øker.")
elif choice1 == "2":
    tillit += 10
    fremdrift -= 5
    print(f"\nDu tar individuelle samtaler. Tilliten øker, men fremdriften går litt tregere.")
else:
    print("Ugyldig valg. Programmet avsluttes.")
    exit()

print(f"Status nå: Fremdrift = {fremdrift}, Tillit = {tillit}\n")
input("Trykk enter for å fortsette...\n")
print("--------------------------------------------------\n")

# --- Beslutning 2: Hamdi og Jabir ---
print("Beslutning 2: Hvordan bør Erling håndtere uenigheten mellom Hamdi og Jabir?")
print("1: Ta initiativ til et felles møte")
print("2: Avvente og ta en beslutning selv uten å inkludere teamet")
choice2 = input("Ditt valg (1/2): ")

if choice2 == "1":
    tillit += 10
    fremdrift += 5
    print("\nErling tar initiativ til møte. Tilliten styrkes og fremdriften øker.")
elif choice2 == "2":
    tillit -= 10
    fremdrift -= 5
    print("\nErling avventer. Konflikten vokser, tilliten svekkes og fremdriften går ned.")
else:
    print("Ugyldig valg. Programmet avsluttes.")
    exit()

print(f"Status nå: Fremdrift = {fremdrift}, Tillit = {tillit}\n")
input("Trykk enter for å fortsette...\n")
print("--------------------------------------------------\n")

# --- Beslutning 3: Motivasjon i teamet ---
print("Beslutning 3: Hvordan kan Erling bevare motivasjonen i teamet?")
print("1: Sette av tid til relasjonsbygging og sosiale aktiviteter")
print("2: Prioritere fremdrift og leveranser")
choice3 = input("Ditt valg (1/2): ")

if choice3 == "1":
    tillit += 15
    fremdrift -= 5
    print("\nErling setter av tid til relasjonsbygging. Tilliten styrkes, men fremdriften går litt ned.")
elif choice3 == "2":
    fremdrift += 15
    tillit -= 5
    print("\nErling prioriterer leveranser. Fremdriften øker, men tilliten svekkes.")
else:
    print("Ugyldig valg. Programmet avsluttes.")
    exit()

print(f"Sluttstatus: Fremdrift = {fremdrift}, Tillit = {tillit}\n")
input("Trykk enter for å fortsette...\n")
print("--------------------------------------------------\n")

# --- Sluttresultat basert på verdiene ---
if fremdrift >= 70 and tillit >= 70:
    print("Teamet gjenoppretter tillit og går videre til norming-fasen.")
elif fremdrift >= 70 and tillit < 70:
    print("Prosjektet leverer fremdrift, men relasjonene er fortsatt sårbare.")
elif fremdrift < 70 and tillit >= 70:
    print("Teamet har god tillit, men mangler fremdrift. Milepælen blir forsinket.")
else:
    print("Prosjektet mister både samhold og fremdrift. Risikoen for forsinkelse er stor.")



