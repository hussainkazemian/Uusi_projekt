# TODO: kysy luku käyttäjältä
# jos luku on alle kaksi, niin koodia on turha suorittaa
number = 3
isPrime = True
for i in range(2, number):
    if number % i == 0:
        isPrime = False
        #print("Numero ei ole alkuluku")
print("alkulukutesti suoritettu")
if isPrime:
    print(f"luku {number} on alkuluku")
else:
    print("Ei ole alkuluku")