import random
valik = ["kivi", "paber", "käärid"]
tulemused = []  
kellega = input("Kahe inimesega või robotiga?").lower()
cound = 1
try:
    if kellega == "kahe inimesi" or kellega == "inimesega" or kellega == "kahe inimesega":
        cound += 1
        mängija = input("Sisesta nimi: ").title()
        mängija2 = input("Sisesta nimi 2: ").title()
    elif kellega == "robotiga" or kellega == "üksi" or kellega == "robootiliselt" or kellega == "robot": 
        cound = 1
        mängija = input("Sisesta nimi: ").title()
    else: 
        print("Provi uuesti!")
        break
clear()
while True:
    try:
        if cound == 1: 
            mängija_valik = input("Sisesta: kivi, paber või käärid: ").lower()
            if mängija_valik == "kivi" or mängija_valik == "käärid" or mängija_valik == "paber":
                robot = random.choice(valik)
                print(f"Robot valis: {robot}")
                if mängija_valik == robot:
                    winner = "Viik"
                elif (mängija_valik == "kivi" and robot == "käärid") or (mängija_valik == "käärid" and robot == "paber") or (mängija_valik == "paber" and robot == "kivi"):
                    winner = mängija
                    tulemused.append(f"{mängija} valis {mängija_valik}, Robot valis {robot}. Võitja: {winner}")
                    print(f"{mängija} on winner!")
                else:
                    winner = "Robot"
                    tulemused.append(f"{mängija} valis {mängija_valik}, Robot valis {robot}. Võitja: {winner}")
                print(f"Võitja: {winner}")
                play_again = input("Kas tahad veel mängida? (jah/ei): ").lower()
                if play_again != "jah":
                    break
            else: 
                print("Vale, proovi uuesti")
        elif cound == 2:
            mängija_valik = input("Sisesta: kivi, paber või käärid: ").lower()
            mängija1_valik = input("Sisesta: kivi, paber või käärid: ").lower()
            if mängija_valik == "kivi" or mängija_valik == "käärid" or mängija_valik == "paber":
                if mängija1_valik == "kivi" or mängija_valik == "käärid" or mängija_valik == "paber":
                    if (mängija_valik == "kivi" and mängija1_valik == "käärid") or (mängija_valik == "käärid" and mängija1_valik == "paber") or (mängija_valik == "paber" and mängija1_valik == "kivi"):
                        winner = mängija
                        print(f"{mängija} on winner!")
                    elif: (mängija_valik == "kivi" and mängija1_valik == "kivi") or (mängija_valik == "käärid" and mängija1_valik == "käärid") or (mängija_valik == "paber" and mängija1_valik == "paber"):
                        winner = "Viik"
                        print("Vikk!")
    except ValueError:
        print("Viga, palun proovige uuesti.")

print("Mängu tulemused:")
for tulemus in tulemused:
    print(tulemus)
