kuha = float(input("Anna kuhun pituus (cm) : "))
if kuha >= 37:
    print("Oko")
elif kuha < 37:
    print("heittää takaisin järveen")
    print("kuha alimmasta puuttuu on (cm):", 37-kuha)