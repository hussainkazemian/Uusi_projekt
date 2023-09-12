"""vuoden_ajat= ("kevät", "kesä", "syksy", "talvi")
kuukaudet = ("jouluku, tammi, maalis",
        "huhti", "touko", "kesäku",
        "heinä", "elo", "syys",
        "loka", "marras", "jouluku")
kuukaudet_luvut = int(input("Anna kuukausi luku (1-12): "))

if kuukaudet_luvut < 1 or kuukaudet_luvut > 12:
    print("virheellinen kaukasi luku.")
else:
    vuoden_ajat = vuoden_ajat [kuukaudet_luvut - 1]
    print(f"kuukausi luku on:  {kuukaudet}.")
"""
"""
vuoden_ajat= ("tammi", "helmi", "maalis",
              "huhti", "touko", "kesäku",
              "heinä", "elo", "syys",
              "loka", "marras", "jouluku")
kuukaudet_luvut = int(input("Anna kuukausi luku (1-12): "))
kuukasi= vuoden_ajat[kuukaudet_luvut-1]
print(f"kuukausi luku {kuukaudet_luvut} on {kuukasi}.")
"""
def main():
    vuodenajat = (
    "talvi", "talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy")

    kuukausi = int(input("Syötä kuukauden numero: "))

    if kuukausi < 1 or kuukausi > 12:
        print("Virheellinen kuukauden numero.")
    else:
        vuodenaika = vuodenajat[kuukausi - 1]
        print("Kuukausi", kuukausi, "kuuluu vuodenaikaan", vuodenaika)


if __name__ == "__main__":
    main()