kuha = float(input("Anna kuhun pituus (cm) : "))
if kuha >= 37: #true/false
    print("Oko, Vois ottaa")
elif kuha < 37:
    print("heittää takaisin järveen")
    print("kuha alimmasta puuttuu on (cm):", 37-kuha)
    print()
