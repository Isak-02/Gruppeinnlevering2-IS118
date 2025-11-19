alder = int(input("Hvor gammel er du? "))

if alder >= 16:
    print("Du kan kjøre berg og dalbane!")
elif alder >= 12:
    med_voksen = input("Har du med noen som er over 16 år? (ja/nei): ")
    if med_voksen == "ja":
        print("Du kan kjøre fordi du har med en voksen over 16 år!")
    else:
        print("Du kan ikke kjøre uten noen over 16 år.")
else:
    print("Du er for ung til å kjøre berg og dalbane.")
