print("kirjoitta oman hyvttiluokaan; a, b, c tai lux:")
käyttäjä = str(input("Anna hyttiluokan: "))
if käyttäjä == "lux" or käyttäjä == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif käyttäjä == "a" or käyttäjä == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif käyttäjä == "b" or käyttäjä == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif käyttäjä == "c" or käyttäjä == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("virhellineen hyttiluokka")