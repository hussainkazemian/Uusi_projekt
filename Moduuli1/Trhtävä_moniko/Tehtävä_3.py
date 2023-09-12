def syota_lentoasema(lentoasemat):
    icao = input("Syötä lentoaseman ICAO-koodi: ")
    nimi = input("Syötä lentoaseman nimi: ")
    lentoasemat[icao] = nimi

def hae_lentoasema(lentoasemat):
    icao = input("Syötä haettavan lentoaseman ICAO-koodi: ")
    if icao in lentoasemat:
        print("Lentoaseman nimi:", lentoasemat[icao])
    else:
        print("Lentoasemaa ei löytynyt.")

def main():
    lentoasemat = {}

    while True:
        print("Valitse toiminto:")
        print("1. Syötä uusi lentoasema")
        print("2. Hae lentoaseman tiedot")
        print("3. Lopeta")

        valinta = input("Valintasi: ")

        if valinta == "1":
            syota_lentoasema(lentoasemat)
        elif valinta == "2":
            hae_lentoasema(lentoasemat)
        elif valinta == "3":
            break
        else:
            print("Virheellinen valinta.")

if __name__ == "__main__":
    main()