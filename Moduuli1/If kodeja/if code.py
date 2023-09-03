rahat = float(input("Anna rahamäärä: "))
ehto = rahat <= 50
print(ehto)
#ehtolause
if rahat >= 50:
    #lohka
    print("sä oot rikas ja voit ostaa jotain.")
if rahat < 50:
    print("et saa ostaa mitään!")
if rahat == 50:
    print("ihan nolla")
#suutari ja räätäli
suutari = input("Anna suutarin nimi:")
räätäli = input("Anna räätäli nimi:")
if suutari == räätäli:
    print("hyvänen aikaa")