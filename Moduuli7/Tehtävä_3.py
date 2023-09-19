#create an empty dictionary to store the airport data:
lentoasemat = {}
#use a while loop to repeatedly ask the user for their
#choice until they choose to quit:
while True:
    käyttäjä = input("valiste letoasema, (1: uusi lentoasema,"
                     "2: lentoasmea_tiedot, 3: lopeta): ")
    if käyttäjä == "1": #code for entering  a new aiport
        icoa_code = input("Anna lentoasemaan icoa code: ")
        nimi = input("Anna lentoasemaan nimi: ")
        lentoasemat[icoa_code] = nimi
        print("lentoasema tallennettu.")
    elif käyttäjä == "2": #code for fetching lentoasema tiedot:
        icoa_code = input("Anna lentoaseman icoa code: ")
        if icoa_code in lentoasemat :
            print("lentoasema nimi: ", lentoasemat[icoa_code])
    else:
        print("virhellinnen valinta. kokeilaan uudeleen")
#for entering a new airport ask the user to the icao code and name
#and store the code in the dictionary.
icoa_code = input("Anna lentoasemaan icoa code: ")
nimi = input("Anna lentoasemaan nimi: ")
lentoasemat[icoa_code] = nimi
#for fetching/appealing lentoasema tiedot ask the user
#to enter icao code and print out the corresonding names:
icoa_code = input("Anna lentoasemaan icoa code: ")
if icoa_code in lentoasemat:
    print("lentoasema nimi on: ", lentoasemat[icoa_code])
    print("virhellinen icoa code.")
#finally when the user choose to quit. the program execution eneds.
#complete the  program:
def main():
    lentoasemat = {}
    while True:
        käyttäjä = input("valiste letoasema (1: uusi lentoasema,"
                         "2: lentoasmea_tiedot, 3: lopeta) :")
        if käyttäjä == "1":  # code for entering a new aiport
            icoa_code =input("anna lentoaseman icao code:")
            nimi = input("Anna lentoasemaan nimi: ")
            lentoasemat[icoa_code] = nimi
        elif käyttäjä == "2":  # code for fetching lentoasema tiedot:
            icoa_code = input("Anna lentoaseman icoa code: ")
            if icoa_code in lentoasemat:
                print("letoasema nimi on :", lentoasemat[icoa_code])
            else:
                print("viirheliinen icoa code.")

        elif käyttäjä == "3":  # code for ends the program:
            break
        else:
            print("virhellinen tiedot. kokeilla uudelleen.")
            main()
