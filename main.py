from laul import Laul
from csv_lugeja import loe_csv_fail

def loo_laulud(tabel):
    laulud = []
    for rida in tabel:
        laul = Laul(rida[0], rida[1], rida[2])
        laulud.append(laul)
    return laulud

def otsi_laulud(laulud, valik, otsitav):
    for laul in laulud:
        if valik == "1" and otsitav.lower() in laul.pealkiri.lower():
            laul.näita()
        elif valik == "2" and otsitav.lower() in laul.esitaja.lower():
            laul.näita()
        elif valik == "3" and otsitav.lower() in laul.kuulamiste_arv.lower():
            laul.näita()

def main():
    tabel = loe_csv_fail("laulud.csv")
    laulud = loo_laulud(tabel)

    kas_jatkata = True
    while kas_jatkata:
        print("Tee valik, kuidas soovid laulu otsida:")
        print("1: otsing laulu pealkirja järgi")
        print("2: otsing artisti järgi")
        print("3: otsing kuulamiste arvu järgi")

        valik = input("Valik [1, 2, 3]: ")

        if valik in ["1", "2", "3"]:
            otsitav = input("Sisesta otsitav: ")
            otsi_laulud(laulud, valik, otsitav)
        else:
            print("Valik ei olnud 1, 2 ega 3. Game over!")
            kas_jatkata = False
        print("++++++++++++++++++++++++++++++++++++++++")

if __name__ == "__main__":
    main()
