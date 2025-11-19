saldo = 100
Pris_kaffe = 20
Pris_kanelboller = 50
Pris_lunchbaguett = 80

print ("Du går på kafe i lunsjen. det er to dager igjen til du får stipend"
       )

print (f"\nDu har følgende saldo på kontoen: {saldo} kr"
       )

print (f"\nPå kafeen har de følgende meny"
       f"\n-kaffe: {Pris_kaffe} kr\n"
       f"-kanelbolle: {Pris_kanelboller} kr\n"
       f"-lunchbaguett: {Pris_lunchbaguett} kr\n"
       )
print("-------------------------------------")
print("du går opp til kassen for å bestille.")

first_choice = input("hvilket produkt kjøper du først?"
                     )

if first_choice == "kaffe":
    saldo = saldo - Pris_kaffe
    print("du mottar kaffen din.")
elif first_choice == "kanelboller":
    saldo = saldo - Pris_kanelboller
    print("du mottar kanelboller")
elif first_choice == "lunchbaguett":
    saldo = saldo - Pris_lunchbaguett
    print("du mottar lunchbaguett")
else:
    print(f"du spør om et ukjent produkt. kafeen har ikke {first_choice},"
          f" Betjeningen ser rart på deg, og du forlater kassen i skam.")
    exit()
    
print (f"du har nå {saldo} kr på konto")


# -----------------del 2 --------------------

print("---------------------------------")
print("\n Du vurdere å kjøpe noe mer.")

second_choice = input("kjøper du noe mer (kaffe, kanelboller, lunchbaguett),"
                      "eller går du for å nyte lunchen(skriv nei)?")

if second_choice == "nei":
    print(f"\n Du forlater kassen me din {first_choice}, og har {saldo} kr igjen på konto.")
elif second_choice == "kaffe":
    if saldo >= Pris_kaffe:
        saldo = saldo - Pris_kaffe
        print(f"Du mottar kaffen din, og har {saldo} kr igjen på konto.")
    else:
        print(f"du hadde ikke nok penger på saldoen, du mangler {saldo - Pris_kaffe} kr"
              f"Det blir litt kleint, du tar me din {first_choice} og forlater kassen.")
        exit()
elif second_choice == "kanelboller":
    if saldo >= Pris_kanelboller:
        saldo = saldo - Pris_kanelboller
        print(f"Du mottar kanelbollen din, og har {saldo} kr igjen på konto.")
    else:
        print(f"du hadde ikke nok penger på saldoen, du mangler {saldo - Pris_kanelboller} kr"
              f"Det blir litt kleint, du tar me din {first_choice} og forlater kassen.")
        exit()
elif second_choice == "lunchbaguett":
    if saldo >= Pris_lunchbaguett:
        saldo = saldo - Pris_lunchbaguett
        print(f"Du mottar lunchbaguetten din, og har {saldo} kr igjen på konto.")
    else:
        print(f"du hadde ikke nok penger på saldoen, du mangler {saldo - Pris_lunchbaguett} kr"
              f"Det blir litt kleint, du tar me din {first_choice} og forlater kassen.")
        exit()
else:
    print(f"du spør om et ukjent produkt, kafeen har ikke {second_choice}."
          f"betjeningen ser rart på deg, og du forlater kassen.")

print(f"du forlater kassen med din {first_choice} og {second_choice} og har {saldo} kr igjen på konto.")

