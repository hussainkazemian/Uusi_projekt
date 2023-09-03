print("kirjoitta oman hyvttiluokaan; a, b, c tai lux:")
käyttäjä = str(input("Anna hyttiluokan: "))
if käyttäjä == "lux":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif käyttäjä == "a":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif käyttäjä == "b":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif käyttäjä == "c":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("virhellineen hyttiluokka")


