"""#funktion rakenne ja kutsuminen
#def=define funktion nimi, (madholloset parametrit)
def tervehti():
    print("Moi!")
    print('nyt ollaan funktion sisällä, ohjelma suortus siirtyi tänne')
    return #tällä palautetaan paluvaro, mikäli sellainen on
#pääohjelma
#Jotta funktion rungossa olevaa koodia suoritettaisin, on funktion kutsutava
print('Terve! tämä on pääohjelma')
#kutustaan funktioda
tervehti()
print('jonka jälkeen tulimme takaisin pääohjelman')

#funktio voi kutsua muita funktioita
def tervehdi_käyttäjä():
    print('Hallo')
    return
def main():
    tervehdi_käyttäjä()
    return
main()

#funktion parametrit
#kerrat = parmetri"
def tervehdi (kerrat):
    for i in range(kerrat):
 print("hyvää päivää" + str (i +1) + ". kerran")
    return
print('päivää aolkaa tervehyksillä.')
    #annetaan argumenti arvo 5"
tervehdi(5)
print('tervehditään lisää.')
    #annetaan argumenti arvo 2
tervehdi(2)

#voidaan kysyä käyttäjälltä
kertaa = int (input('montako kertaa terveyhditään?'))
tervehdi(kertaa)

#funktion parametrit ja paluarvo

def printta_summa(x , y):
    print(x + y)
    return

#funktion voi välittää useampia argumenrreja
#tämä funktio ei palauta mitää, joskus tämä on ihan ok
printta_summa(5, 8)

def summa(x,y):
    yht = x + y
    return yht
tulos= summa(4, 55)
print(tulos)
"""
#muita piirteitä
def tieto (nimi, ikä, harrastus):
    tervehdys =f'Hallo {nimi}. ikäsi on {ikä}. harrastuksesi on {harrastus}.'
    return tervehdys
henkilö = tieto('hussain', 30,'lukemista')
print(henkilö)
#parametrin välittäminen avainsanojen avulla
#ohjelmota voi antaa parametrin arvot (nimi =arvo) -parena
#parametrille voi antaa funktion määrityksessä myös oletusarvo
henkilö2 = tieto(nimi='Sari', ikä= 40, harrastus='Jälkopalo')
print(henkilö2)
#mitä jos on tiedä jotain argumenti, miten voin kutsua funktioda??
def tieto2 (nimi, ikä, harrastus='ohjelmointi'):
    tervehdys =f'Hallo {nimi}. ikäsi on {ikä}. harrastuksesi on {harrastus}.'
    return tervehdys
henkilö3 = tieto2('Ulla', 28)
print(henkilö3)