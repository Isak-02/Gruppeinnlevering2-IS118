
tillit=1
fremdrift=0

print("--------------------------------------------------"
    "\nHei Erling, du er i gang med et prosjekt med et nytt team. "
    "\nFørst synes du alt i teamet gikk fint, "
    "\nmen nå har det oppstått konflikter blant gruppe medlemmene."
)
print("---------------------------------"
    f"\nDu har startet teambuilding, teamet liker deg, du har fått {tillit} tillit så langt"
    f"\nFremdrifter ligger på {fremdrift} du må nå 10 for å fullføre prosjektet innen fristen."
)
input("Trykk Enter for å fortsette...")
print("------------------------------------")

print(
    "\nOi det har oppstått en konflikt mellom Silje og Sivert!" 
    "\nDe er uenige om teknologivalg og design, " 
    "\ndette har utviklet seg fra en sakskonflikt til en personkonflikt."
    "\n----------------------------------------------------------"
)
input("Trykk Enter for å fortsette...")
print(
    "\nDette er valgene du kan ta:" 

    "\nA: Skal han ta det opp i plenum for å skape åpenhet?"
    "\nB: Skal han ta individuelle samtaler for å dempe temperaturen?"
    "\nC: Eller skal han la HR bistå for å sikre en nøytral håndtering?"
    "\nD: Finne en middel-ground i konflikten som alle kan bli enig om."
)


#If settninger for å vise utfall av de forskjellige valgene.
first_choice = input("\nHvilket valg velger du (A, B, C, D)?").strip().upper()
print("------------------------------------------------------------")
if first_choice == "A":
    fremdrift = fremdrift + 4
    tillit = tillit + 2
    print("\nDu velger A, å ta det opp i plenum for å skape åpenhet")
    print("Teamet setter pris på at du tar det opp, og går igjennom saken sammen, du mottok 3 tillit")
elif first_choice == "B":
    fremdrift = fremdrift + 2
    tillit = tillit + 3
    print("\nDu valgte B, å ta en individuell samtale for å dempe temperaturen.")
    print("Selv om det hjelper litt for fremdriften i prosjektet, så ligger det forsatt sure " 
    "miner hos begge partene.")
elif first_choice == "C":
    fremdrift = fremdrift + 3
    tillit = tillit - 1
    print("\nDu valgte C, la HR sikre en nøytral håndtering")
    print("Ordet sprer seg og teamet syns at du ikke bryr deg om arbeidsmiljøet.")
elif first_choice == "D":
    fremdrift = fremdrift + 4
    tillit = tillit + 5
    print("\nDu valgte D, å finne en middle-ground som alle kan bli enige om ")
    print("Teamet liker forslaget ditt, Silje of Sivert har kommet overens")
else:
    fremdrift = fremdrift - 100
    tillit = tillit - 100
    print("\nDu klarer ikke ta et valg og ser ut som en dust foran laget.")
    print("De tror du er for inkompetent for rollen som leder.")
    print(f"Du har {tillit} fra teamet og prosjektet ligger på {fremdrift}, du er en elendig leder.")
    exit()

print(f"\nDin nye tillit blant teamet er {tillit} og prosjektet har en framdrift på {fremdrift} så langt!")
input("\nTrykk Enter for å fortsette...")
print("--------------------------------------------------------------")

print("Etter at du løste konflitken mellom Silje og Sivert, oppstår det en ny konflikt mellom Hamdi og Jabir.")
print("\nDe er uenige om hvordan innbyggerne skal kunne delta i digitale folkemøter")
print("Foreløpig er konflikten minimal, men du kjenner at frustasjonen vokser,")
print("fristen på første prototype nærmer seg, stemningen er spent.")

input("\nTrykk Enter for å fortsette...")
print("------------------------------------------------------------------------------")


print(
    "\nDette er valgene du kan ta:"

    "\nA: Skal han vente og håpe at partene finner en løsning selv?" 
    "\nB: Skal du ta initiativ for å ta opp situasjonen i et fellesmøte?" 
    "\nC: Ikke ta siden til noen av partene, men heller din egen idé, du vet jo best?"
)
second_choice = input("\nHvilket valg velger du?").strip().upper()
print("------------------------------------------------------------")
if second_choice == "A":
    fremdrift = fremdrift + 1
    tillit = tillit + 3
    print("\nDu valgte A, å vente til begge partene finner ut av det selv.")
    print("Selv om det hjelper litt for fremdriften i prosjektet, " \
    "\nså ligger det forsatt sure miner hos begge partene.")
elif second_choice == "B":
    fremdrift = fremdrift + 2
    tillit = tillit + 5
    print("\nDu valgte B, å ta initiativ for å ta opp situasjonen i et fellesmøte.")
    print("Teamet setter pris på at du tar initiativ for å ordne opp, de synes du er en god leder.")
elif second_choice == "C":
    fremdrift = fremdrift - 5
    tillit = tillit - 5
    if tillit >= 0:
        print("\nDu valgte C, ikke ta siden til noen, siden du vet best")
    else:
        print("\nTeamet har mistet troa i deg, de rappoterte deg til HR.")
        print("Du mistet jobben og skammer deg over livet ditt")
else:
    fremdrift = fremdrift - 100
    tillit = tillit - 100
    print("\nDu klarer ikke ta et valg og ser ut som en dust foran laget.")
    print("De tror du er for inkompetent for rollen som leder.")
    print(f"Du har {tillit} fra teamet og prosjektet ligger på {fremdrift}, du er en elendig leder.")
    exit()
#Koden over altså "else" bruker en exit for å slutte koden, fordi det er egentlig "Game Over"

print(f"\nDin nye tillit blant teamet er {tillit} og prosjektet har en framdrift på {fremdrift} så langt!")
input("\nTrykk Enter for å fortsette...")
print("-------------------------------------------------------------------")

print("\nEtter konfliktene, ønsker Erling å bevare motivasjonen i teamet fram til fristen.")
print(
    f"\nDu har en tillit i teamet på {tillit}, og prosjektet har {fremdrift}."
      "\nDitt utfall vil bli avklart etter neste spørsmål." \
      "\nVelg med omhu..."
)
input("\nTrykk Enter for å fortsette...")
print("\n--------------------------------------------------------------")

print("Dette er valgene du kan ta, fristen nærmer seg:"
      "\nA: La teamet jobbe overtid for å sikre ferdig prototype før jul."
      "\nB: Dra ut på byen, du har fortjent det, prosjektet er jo snart ferdig!"
      "\nC: Jobbe med prosjektet så mye som mulig, " 
      "\nmen ta av noen dager for kos, hygge og sosiale aktiviteter."
)

third_choice = input("\nHva velger du(A, B, C)?").strip().upper()

if third_choice == "A":
    fremdrift = fremdrift + 5
    tillit = tillit - 6
    if tillit <= 5:
        print("\nDu har settet teamet ditt under masse press. De er misfornøyde."
              "\nHR sier du har fått så mye negative tilbakemeldinger at du får sparken.")
        exit()
    else:
        print("\nDu valgte A, å la arbeiderne jobbe overtid. " 
        "\nIngen vil kanskje bli med på laget ditt til neste gang, men du ble ihvertfall ferdig.")
        print(f"\nDin nye tilliet er {tillit} og prosjektet har en fremdrift på {fremdrift}.")
elif third_choice == "B":
    fremdrift = fremdrift - 1
    tillit = tillit - 1
    if fremdrift <= 5:
        print("Du valgte B, og har sendt teamet ditt til fiasko. Dere ble aldri ferdig med prosjektet." \
        "Du har ikke tatt jobben seriøst, eller så bryr du deg ikke nok.")
        exit()
    else:
        print("Du valgte B, å dra ut på byen siden prosjektet er snart ferdig.")
        print (f"Du har {tillit} tillit, og prosjektet er på {fremdrift}.")
else:
    fremdrift = fremdrift + 5
    tillit = tillit + 5
    print("Du valgte C, å jobbe så mye som mulig, men å forsatt ha fritid.")

print("-------------------------------------------------------------------")

print("\nNå har du svart på alle spørsmålene Erling, nå skal vi se hva slags leder du er." \
    "\nOg hva som har gått rett eller galt.")

input("\nTrykk Enter for å fortsette...")
print("--------------------------------------------------------------")

#Her sjekker koden om en eller flere av kravene er oppfylt. For å få en "halveis" god slutt på historien
if fremdrift >= 10 and tillit >= 10:
    print("\nDu og teamet ble ferdig med prosjektet i god tid før fristen!" \
    "\nDu har hatt en demokratisk lederstil, du har klart å balansere situasjonene bra." 
    "\nTeamet synes du er en god leder, du klarte å få best mulig utfall i historien!")
elif fremdrift >= 10 or tillit >= 10:
    if fremdrift >= 10 and tillit < 10:
        print("Du ble ferdig med prosjektet i god stund. Men teamet vil ikke arbeide med deg igjen." 
        "\nDe synes lederstilen din er for autoritær.")
    else:
        print("\nDu hadde ikke det beste utfallet i prosjektet, dere stress jobbet mye før fristen." 
        "\nDu var stresset og følte du aldri skulle bli ferdig")
        print("Teamet var med deg hele veien, og de tok seg tid i fritiden for å hjelpe å bli ferdig."
              "\nDu var kanskje litt for grei, og lot ting bare skli. Du har vært en la det skure leder.")
else:
    print("Du klarte ikke å bli ferdig med prosjektet og har heller ikke nok tillit hos teamet ditt." 
    "\nDe var ikke interesert i å jobbe med deg mer, "
    "\nog du har blitt stempla som Værste planlegger og leder i prosjekt arbeid-bransjen i avisen.")