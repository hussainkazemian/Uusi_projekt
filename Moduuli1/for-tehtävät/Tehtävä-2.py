luvut = []
luku = True
while luku:
    syöte = input("kirjoitta numero tai lopetta painamalla Enter:")
    if syöte != "":
        luvut.append(int(syöte))
    else:
        luku = False
print(luvut)
luvut.sort(reverse=True)
print(luvut[0:5])