# skår system

Samarbeid_skåre = 0

# feil input sjekk

feil_input = False

# itroduksjon og valg 1

print("Velkommen til erlings storyline")
print("Du er prosjektleder erling og må nå ta tak i diverse konflikter for at teamet skal rekke deadlinene som nærmer seg med stormskritt")
print("første konflikt er silje og siverts uenighet om teknologi")
print("Du står foran to valg.")
print ("1: ta da opp med hele teamet i fellekap")
print("2: hold en inviduel samtale med hver av dem")

valg1 = input("Skriv 1 eller 2")

# sjekk for feil input og print av svar 

if valg1 not in ("1", "2"):
    feil_input = True

if valg1 == "1":
    print("du valgte å ta det opp i plenum foran hele teamet")
    print("konsekvens: konflikten er nå synlig, men fremdriften øker")
    Samarbeid_skåre += 1
elif valg1 == "2":
    print("du valgte å ta individuelle samtaler med sivert og silje hver for seg")
    print("konsekvens: Tilliten øker, men fremdriften går litt tregere")
    Samarbeid_skåre += 1

# valg 2 

print("du møter nå konflikt 2 mellom Hamdi og Jabir")
print("de er uenige om hvordan kommunen skal gjennomføre digitale folkemøter")
print("her har du også 2 valg")
print("1: Du aventer å håper de finner ut av det selv")
print("2: Du velge å ta en besluttning selv uten å involvere teamet")

valg2 = input("skriv 1 eller 2")

# sjekk for feil input og print av svar

if valg2 not in ("1", "2"):
    feil_input = True

if valg2 == "1":
    print("du valgte å avente og håpe de finner ut av det selv")
    print("konsekvens: de løser konflikten, men det er forsatt klein stemning mellom dem")
    Samarbeid_skåre += 1
elif valg2 == "2":
    print("du valgte å ta en besluttning selv uten å involvere teamet")
    print("kosekvens: ingen av dem føler seg hørt, men prosjektet har god fremdrift")
    Samarbeid_skåre -= 1


# valg 3

print("etter alt dette merker du at motivasjoen i teamet er lavere en normalt, hvordan angriper du dette?")
print("som vanelig har du 2 valg")
print("1: du velger å fokuser på relasjonbygging og teamfokus")
print("2: du fokuserer på fremdrift og leveranse")

valg3 = input("skriv 1 eller 2")

# sjekk for feil input og print av svar

if valg3 not in ("1", "2"):
    feil_input = True

if valg3 == "1":
    print("du valgte å fokusere på relasjonsbygging og teamfokus")
    print("konsekvens: bedre samarbeid og sosialt klima, men risiko for lavere fremdrift")
    Samarbeid_skåre += 1
elif valg3 == "2": 
    print("du valgte å fokusere på fremdrift og leveranse")
    print("konsekvens: prosjektet kommer videre, men teamet risikerer langvarige sammarbeidsproblemer")
    Samarbeid_skåre -= 1

# konklusjon og resulatt utregning, samt at det vil kome feil melding ved ugyldig input, feks bokstav eller et annet tall enn 1 og 2

if feil_input:
    print("du har skrevt en annen verdi enn 1 eller 2 i et av valgene, vennligst clear og prøv igjen")
else:
    print("konkluson")
    if Samarbeid_skåre < 0:
        print("teamet fungerer dårlig og dere rekker ikke milepælen, Takk for at du spilte!")
    elif Samarbeid_skåre == 0 or Samarbeid_skåre == 1:
        print("teamet fungerer ok, og dere rekker akkurat milepælen, Takk for at du spilte!")
    else:
        print("teamet fungerer veldig godt og dere rekker milepælen, Takk for at du spilte!")  



