luku = input("anna joku luku:")
min = max = luku

while luku !='':
    luku = float (luku)
    min = float (min)
    max = float (max)
    if luku < min:
        min= luku
    if luku > max:
        max = luku
    luku = input("anna seurava luku")

print(f'''
{min} - on pienin sinun luvuista
{max} - on isoin sinun luvuista ''')

