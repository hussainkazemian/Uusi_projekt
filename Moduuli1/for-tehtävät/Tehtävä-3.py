number = int(input("Kirjoitta numero: "))
is_Prime = True
for i in range(1, number):
    if number % i == 0:
        isPrime = False
print("alkulukutesti suoritettu")
if is_Prime:
    print(f"luku {number} on alkuluku")
else:
    print("Ei ole alkuluku")