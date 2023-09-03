
print('koira haukuu koko ajan. vöit käskeä sitä lopettamaan')
käsky = input('Anna käsky, jos annat (stop) lopettaa :\n')

while käsky != 'stop':
    if käsky == 'apua':
        break
    kerrat = 0
    while kerrat < 10:
        print('koira haukuu hoyyyhoeyyyy')
    kerrat +=1
    käsky = input('Anna käsky, jos annat (stop) lopettaa :\n')
else:
    print('anna käslyn stop ja koita loppetti')

#uusi tutkinta
    import random

    noppa1 = noppa2 = heitot = 0
    while noppa1 != 6 or noppa2 != 6:
        noppa1 = random.randint(1, 6)
        noppa2 = random.randint(1, 6)
        heitot = heitot + 1
    print(f"Tarvittiin {heitot:d} heittoa.")


