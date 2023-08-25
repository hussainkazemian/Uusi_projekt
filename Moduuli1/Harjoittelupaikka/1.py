print('morjesta, maailma!')
print("Hello, from other side!")
print('"hei! kerrotaan", vastakaa!')
print("hyvää")
print("päivää")
print("hyvaa\npaivaa")
käyttäja =input("kuka olet?: ")
print("hauska tavata!, " + käyttäja + "!")
käyttäja2 = input("Anna nimisi? : ")
print("hasuka tavata!," + käyttäja2 + "!")
eka = -9
toka = 12_541_5412_54
kolmas = 5.544
neljas = -7 + 5j
print()
print(eka)
print(toka)
print(kolmas.real)
print(neljas.imag)
print()
fahrenheit_str = input("Anna lampotila Fahrenheit-asteina: ")
fahrenheit = float(fahrenheit_str)
celsius = (fahrenheit - 32) * 5/9
print("lampotila celsius-asteina:" + str(celsius))
print()
print(f"lampotila celsius-asteina: {celsius}")
print()
print(f"lampotila celsius-asteina: {celsius:6.3f}")
print()
import math
print(f"{'pii':12s}:{math.pi:10.5f}")
print(f"{'neperin luku':12s}:{math.e:10.5f}")