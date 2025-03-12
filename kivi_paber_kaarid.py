import random

valik = ["kivi", "paber", "käärid"]
tulemused = []  
kellega = input("Kahe inimesega või robotiga? ").lower()
count = 1
viik = 0 
countmang1 = 0
countmang2 = 0

if kellega in ["kahe inimesi", "inimesega", "kahe inimesega"]:
    count = 2
    mängija = input("Sisesta nimi 1: ").title()
    mängija2 = input("Sisesta nimi 2: ").title()
elif kellega in ["robotiga", "üksi", "robootiliselt", "robot"]:
    count = 1
    mängija = input("Sisesta nimi: ").title()
else: 
    print("Proovi uuesti!")
    exit()

print("Mäng alustati! Kirjutage 'stopp', et lõpetada mäng.")

while True:
    try:
        if count == 1: 
            mängija_valik = input("Sisesta: kivi, paber või käärid (või 'stopp' lõpetamiseks): ").lower()
            if mängija_valik == "stopp":
                break
            if mängija_valik in valik:
                robot = random.choice(valik)
                print(f"Robot valis: {robot}")

                if mängija_valik == robot:
                    winner = "Viik"
                    viik += 1
                    print("Viik!")
                elif (mängija_valik == "kivi" and robot == "käärid") or \
                     (mängija_valik == "käärid" and robot == "paber") or \
                     (mängija_valik == "paber" and robot == "kivi"):
                    winner = mängija
                    countmang1 += 1
                    print(f"{mängija} on võitja!")
                else:
                    winner = "Robot"
                    countmang2 += 1
                    print("Robot on võitja!")

                tulemused.append(f"{mängija} valis {mängija_valik}, Robot valis {robot}. Võitja: {winner}")
            else: 
                print("Vale valik, proovi uuesti.")

        elif count == 2:
            mängija_valik = input(f"{mängija}, sisesta: kivi, paber või käärid (või 'stopp' lõpetamiseks): ").lower()
            if mängija_valik == "stopp":
                break
            mängija1_valik = input(f"{mängija2}, sisesta: kivi, paber või käärid (või 'stopp' lõpetamiseks): ").lower()
            if mängija1_valik == "stopp":
                break

            if mängija_valik in valik and mängija1_valik in valik:
                if mängija_valik == mängija1_valik:
                    winner = "Viik"
                    viik += 1
                    print("Viik!")
                elif (mängija_valik == "kivi" and mängija1_valik == "käärid") or \
                     (mängija_valik == "käärid" and mängija1_valik == "paber") or \
                     (mängija_valik == "paber" and mängija1_valik == "kivi"):
                    winner = mängija
                    countmang1 += 1
                    print(f"{mängija} on võitja!")
                else:
                    winner = mängija2
                    countmang2 += 1
                    print(f"{mängija2} on võitja!")

                tulemused.append(f"{mängija} valis {mängija_valik}, {mängija2} valis {mängija1_valik}. Võitja: {winner}")
            else:
                print("Vale valik, proovi uuesti.")

    except ValueError:
        print("Viga, palun proovige uuesti.")
print("Kokkuvõte:")
print(f"{mängija} võite: {countmang1}")
print(f"{mängija2 if count == 2 else 'Robot'} võite: {countmang2}")
print(f"Viike: {viik}")
print("Mäng on lõppenud. Aitäh mängimast!")
