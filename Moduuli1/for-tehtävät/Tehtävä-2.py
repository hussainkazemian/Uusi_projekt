luvut = []
luku = input("kirjoitta numero tai lopetta painamalla Enter:")
while luku!="":
    luvut.append(luku)
    luku = input("kirjoitta numero tai lopetta painamalla Enter:")
luvut.sort(reverse=True)
print(luvut)