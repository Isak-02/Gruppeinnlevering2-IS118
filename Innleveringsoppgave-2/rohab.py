# -------------- Bakgrunns historie -------------------- 

#Det har gått seks uker siden Erling, prosjektleder for utviklingen av kommunens nye digitale medborgerportal,
# samlet sitt prosjektteam for første gang. 
# Etter en inspirerende oppstart med høy energi, begynner samarbeidet nå å møte sine første reelle prøver. 
# I starten var stemningen god. Gruppen opplevde høy motivasjon og fellesskap i målet 
# om å lage en portal som kunne øke innbyggerengasjement og transparens i kommunen. 
# Men nå, etter seks uker, har prosjektet gått inn i den klassiske storming-fasen, 
# der ulike faglige perspektiver og personlige preferanser begynner å kollidere. 
# Det har oppstått konflikt mellom flere parter i teamet, 
# og du må hjelpe Erling med å velge det beste valget for å sørge for at teamet 
# kan fikse opp i konflikten og gå videre til performing-fasen.



# --------------------- intro -------------------------------------
print("")
# poeng system som skal bli brukt for siste tre ulike utfall
gode_valg = 0 

#printe ut intorduskjons tekst til bruker 
print("Tusen takk for at du vil hjelpe Erling med å håndtere konflikter i teamet sitt")
print("Du vil bli møtt med to alternativer, og din rolle er å velge en av de to")
print("Målet er å hjelpe Erling å unngå å forverre konfliktene, og fokusere på å løse konfliktene")
print(" ")



# -------------------- konflikt mellom silje og sivert ------------

# importere kommando, gir infor om python modul 
import sys
print("DEL1: Det har opstått en konflikt mellom Silje og Sivert, velg en av alternativene som vil hjelpe Erling i å løse konflikten") 
print("Alternativ 1: Erling kan velge å ta dette opp i plenum sammen med resten av teamet")
print("Alternativ 2: Erling kan ta individuelle samtaler med Silje og Sivert")

#lagrer brukerens input i variabel valg1 
valg1 = input("\nVelg mellom 1 eller 2") 

#hvis brukeren har skrevet 1, skriver koden ut konsekvensen av dette valget
if valg1 == "1":
    print("Konsekvens -> Erling tar det opp i plenum. Konflikten blir synlig, og fremdriften øker. \nMen nå har et nytt konflikt mellom Hamdi og Jabir opstått")

#hvis brukeren har skrevet 2, skriver koden ut konsekvensen av dette valget
elif valg1 == "2":
    print("Konsekvens -> Erling tar individuelle samtaler. Tilliten øker, men fremdriften går litt tregere. \nMen nå har et nytt konflikt mellom Hamdi og Jabir opstått")

#hvis brukeren skrev inn noe annet enn 1 eller 2 vil føre til at brukeren må prøve på nytt  
else: 
    print(f"du kan bare velge mellom alternativ 1 eller 2, start på nytt!")
    sys.exit()



# ------------------- konflikt mellom Hamdi og Jabir --------------

print("")
#lagrer brukerens valg i variabel start_choice
start_choice = input("Er du klar til å starte å løse neste konflikt? (Ja/Nei)")

#sjekker om brukeren skrev ja 
if start_choice == "Ja":
    print("\nDEL2: Konflikten mellom Hamdi og Jabir handler om uenighet om hvordan inbyggerne skal kunne delta i digitale folkemøter.\nHvilket alternativ bør Erling følge??")
    print("Alternativ 1: Erling avventer og håper på at partene finner en løsning selv")
    print("Alternativ 2: Erling kan ta en beslutning selv uten å inkludere teamet")

#sjekker om brukeren skrev nei og avslutter programmet
elif start_choice == "Nei":
    print("Du kan komme tilbake når du er klar!") (sys.exit())

#skrev brukeren noe annet enn ja eller nei vil programmet avsluttes
else: 
    print("Jeg beklager, jeg tar bare imot ja/nei svar, du kan prøve på nytt")
    sys.exit()

valg2 = input("")
#sjekker om brukeren skrev inn 1, og printer konsekvens dersom ja 
if valg2 == "1":
    print("Konsekvens -> Hamdi og Jabir løser konflikten, men det er klein stemning mellom partene")

#sjekker om brukeren skrev inn 2 og printer ut konsekvens dersom ja 
elif valg2 == "2":
    print("Konsekvens -> Hamdi og Jabir føler seg ikke hørt, men prosjektet har god fremdrift") 


# ------------------------ fraværende motivasjon -----------------------------------
print("")

#spør om brukeren vil fortsette 
start_choice = input("Etter alle konfliktene har motivasjons nivået vært fallende. vil du hjelpe til en siste gang? (Ja/Nei)")

#hvis ja vil informasjon om scenarioet skrives ut 
if start_choice == "Ja":
    print("Erling står ovenfor to alternativer han kan velge for å prøve å øke motivasjonen i teamet igjen. Hva er best i dette scenarioet?")
    print("Alternativ 1: Erling kan velge å fokusere på relasjonsbygging og teamfokus")
    print("Alternativ 2: Erling velger å fokusere på fremdrift og leveranse")

#hvis nei vil koden avsluttes 
elif start_choice == "Nei":
    print("Du kan komme tilbake når du er klar!") (sys.exit())

#noe annet enn ja eller nei vil føre til at brukeren må prøve på nytt  
else: 
    print("Jeg beklager, jeg tar bare imot ja/nei svar, du kan prøve på nytt")
    sys.exit()

valg3 =input("")

#sjekker om brukeren skrev inn 1 og printer ut konsekvens 
if valg2 == "1":
    print("Konsekvens -> Bedre samarbeid og sosialt klima, men risiko for litt lavere fremdrift.")

#sjekker om brukeren skrev inn 2 og printer ut konsekvens 
elif valg2 == "2":
    print("Konsekvens -> Prosjektet kommer videre, men teamet risikerer langvarige samarbeidsproblemer") 


# --------------------- Konklusjon  --------------------

#sjekker om brukeren gjorde godt valg i valg1
if valg1 == "2":
#øker telleren med en dersom det ble gjort et godt valg 
    gode_valg += 1

#sjekker om brukeren gjorde godt valg i valg2
if valg2 == "1":
#øker telleren med en dersom det ble gjort et godt valg 
    gode_valg += 1

#sjekker om brukeren gjorde godt valg i valg3
if valg3 == "1":
#øker telleren med en dersom det ble gjort et godt valg 
    gode_valg += 1

#regner ut om gode valg er 2 eller fler 
if gode_valg >= 2:
    print("Teamet gjenompretter tillit og går videre til norming fasen")

#regner ut om gode valg er lik 1 
elif gode_valg == 1:
    print("Konflikten løses delvis, men relasjonen er fortsatt sårbare")

#hvis brukeren ikke har gjort noen gode valg  
else:
    print("prosjektet mister samhold og forsinkes")