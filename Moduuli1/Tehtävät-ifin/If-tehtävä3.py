print("kirjoittaa M, jos olet miehen")
print("kirjoittaa N, jos olet nainen")
print("kirjoittaa R, jos et ole M ja N")
käyttäjä = str(input("Anna sinun biologisen sukupuolen: ?"))
hl = float(input("Anna sinun hemogolobiinarvo: ?"))
if käyttäjä and hl < 134:
    print("käyttäjä on: Mies ja hemogolobiinoarvo on alhainen")
elif käyttäjä and hl in range (134, 195):
    print("kayttäjä on: Mies ja hemogolobiinarvo on normaali")
elif käyttäjä == "M" and hl > 195:
    print("käyttäjä on: Mies ja hemogolobiinarvo on korkea")
elif käyttäjä and hl < 117:
    print("käyttäja on Niaset ja hemogolobiiniarvo on alhainen")
if käyttäjä == "N" and hl in range(117, 175):
    print("käyttäjä on Naiset ja hemogolobiiniarvo on normaali")
elif käyttäjä and hl >175:
    print("käyttäjä on naiset ja hemogolobiiniarvo on korkea")
else:
    print ("Anna uudellen oikein sukupuoli")


