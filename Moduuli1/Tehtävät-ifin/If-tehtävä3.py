print("kirjoittaa M, jos olet miehen")
print("kirjoittaa N, jos olet nainen")
print("kirjoittaa R, jos et ole M ja N")
käyttäjä = str(input("Anna sinun biologisen sukupuolen: ?"))
hl = int(input("Anna sinun hemogolobiinarvo: ?"))
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

"""
sp = input( "anna biologinen sukupuolisi (m/n): ").lower()
hmglob = input("anna hemogolobiiniarvosi (g/l: ")
if  sp == "m":
    if int (hmglob) < 134:
        hmglob = "alhainen"
    elif 134>= int(hmglob)>=195:
        hmglob = "normalli"
    elif 195 < int (hmglob):
        hmglob = "korkea"
    elif sp == "n":
      if int(hmglob) < 117:
            hmglob = "alhainen"
    elif 134 >= int(hmglob) >= 175:
            hmglob = "normalli"
    elif 175 < int(hmglob):
            hmglob = "korkea"
    print(hmglob)
"""

