## create a tuple to store the seasons as strings:
vuoden_ajat= ("kevät", "kesä", "syksy", "talvi")
#ask the user to enter a number represnting a month:
kuukaudet= int(input("Anna kuukausi luku (1-12): "))
#determine the season based on the inputted month:
if kuukaudet in (12, 1, 2):
    kausi = vuoden_ajat[0] #talvi
elif kuukaudet in (3, 4, 5):
    kausi = vuoden_ajat[1] #kevät
elif kuukaudet in (6, 7, 8):
    kausi = vuoden_ajat[2] #kesä
elif kuukaudet in (9, 10, 11):
    kausi = vuoden_ajat [3] #syksy
else:
    print("virheellinen kuukauden luku.")
    exit()
#print out the corresponding season:
print(f"kuukaudelle {kuukaudet} on vuodenaika {vuoden_ajat}")
#put all together
def main():
    vuoden_ajat = ("kevät", "kesä", "syksy", "talvi")
    kuukaudet = int(input("Anna kuukauden numero (1-12): "))
    if kuukaudet in (12, 1, 2):
        kasui = vuoden_ajat[0]  # talvi
    elif kuukaudet in (3, 4, 5):
        kausi = vuoden_ajat[1]  # kevät
    elif kuukaudet in (6, 7, 8):
        kausi = vuoden_ajat[2]  # kesä
    elif kuukaudet in (9, 10, 11):
        kausi = vuoden_ajat[3]  # syksy
    else:
    #if the month is not based on inputted month (1-12) print an error.
        print("virheellinen kuukauden luku.")
        exit()
    print(f"kuukaudelle {kuukaudet} vuodenaika {vuoden_ajat}")
    main()


"""
kuukaudet = ("jouluku, tammi, maalis",
        "huhti", "touko", "kesäku",
        "heinä", "elo", "syys",
        "loka", "marras", "jouluku")

if kuukaudet_luvut < 1 or kuukaudet_luvut > 12:
    print("virheellinen kaukasi luku.")
else:
    vuoden_ajat = vuoden_ajat [kuukaudet_luvut - 1]
    print(f"kuukausi luku on:  {kuukaudet}.")
"""
"""vuoden_ajat= ("tammi", "helmi", "maalis",
              "huhti", "touko", "kesäku",
              "heinä", "elo", "syys",
              "loka", "marras", "jouluku")
kuukaudet_luvut = int(input("Anna kuukausi luku (1-12): "))
kuukasi= vuoden_ajat[kuukaudet_luvut-1]
print(f"kuukausi luku {kuukaudet_luvut} on {kuukasi}.")
"""
"""def main():
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
"""