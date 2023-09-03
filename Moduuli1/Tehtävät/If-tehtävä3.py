print("kirjoittaa M, jos olet miehen")
print("kirjoittaa N, jos olet nainen")
print("kirjoittaa R, jos et ole M ja N")
sukupuoli = str(input("Anna sinun biologisen sukupuolen: ?"))
hemogolobiinarvo = str(input("Anna sinun hemogolobiinarvo: ?"))
if sukupuoli == "M" and hemogolobiinarvo < 134:
    print("käyttäjä on: Mies ja hemogolobiinarvo on alhainen")
elif sukupuoli == "M" and hemogolobiinarvo >=195:
    print("käyttäjä on: Meis ja hemogolobiinarvo on korkea")
elif sukupuoli == "M" and 134 <= hemogolobiinarvo <= 195:
    print ("käyttäjä on: Mies ja hemogolobiinarvo on normaali")
   # print("käyttäjä on: muuta biologisen sukupuolen ryhmä")#and hemogolobiinarvo >=134 and hemogolobiinarvo <= 195: