import math
name = input("kuka olet?")
print(name)
age = input ("kirjoitta ika?")
print(age)
print(name + ",ikä: :" + str(age))
age = input("kuinka vanha olet?")
print("Moi " + name + ", olet" + age + "vuotta vanha.")
#muutetaan kayttajan syottama stringi kokonaisluviuksi (int) jalisaatan 1
new_age =int(age) + 1
print("vuoden paasta olet" + str(int(age) + 1) + "vuotta.")
#toinen tapa ydhella rivilla
#print("vuoden paasta olet " + str(int(age) + 1) + "vuotta."
#jakolaskukone
num1 = int(input ("Anna jaettava luku?"))
num2 = int(input("Anna jakaja:"))
result=num1 * num2
print("jakolaskun tulos: " + str(result))
print(f"jakolaskun tulos: {result: 8.2f}")
print(f"jakolaskun tulos :{result: 8.5f}")

print("piin arvo {math.pi}")
# ympyran ala
#r=5
#area = math.pi *r*r