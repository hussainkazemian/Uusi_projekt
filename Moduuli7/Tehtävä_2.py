#create a set data structure to store the names:
nimet = set()
#using a while loop to ask the user for names until
# enter an empty strings endes the program:
while True:
    nimi = input("kirjoitta nimiso (tyhjää lopettaa): ")
    if nimi == "":
        break
    else:
#check if the name is already in the set:
        if nimi in nimet:
            print("nimi on listasta")
        else:
            print("uusi nimi")
#add the name to the set:
        nimet.add(nimi)
#print out the input names one by one in any order:
    print("aiemmin kirjoittat nimi: ")
    for nimi in nimet:
        print(nimi)
def main():
    nimet = set()
    while True:
        nimi = input("kirjoitta nimisi (tyhjänä lopettaa): ")
        if nimi == "":
            break
        else:
            if nimi in nimet:
                print("nimi on listasta")
            else:
                print("uusi nimi")
            nimet.add(nimi)
    print("aiemmin kirjoittat nimi ")
    for nimi in nimet:
        print(nimi)
    main()
# in the main program we define the set data structure
#"nimet" to store the input nimet:
#we use a loop that continue indefinitly until the
#user enters an empty string.

