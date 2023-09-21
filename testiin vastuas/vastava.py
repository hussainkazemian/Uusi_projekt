"""
n = 0
for outer in range(3,0,-1):
    m=0
    for inner in [2,0,2,3]:
        if (outer == inner):
            m += 1
        n += 1
    print(m)
print(n)
"""
"""
(red, blue) = (8,5)
coulurs = red, blue
print(coulurs[1])
print(blue)
print(coulurs)
"""
import random
"""def greeting (nimi):
    return f"Heelo, {nimi}!"
def cast_dice (noppa, ivu):
    summa =0
    for i in range (noppa):
"""
import random
command = input("Enter command: ")
while command!="stop":
    if command=="MAYDAY":
        break
    print("Executing command: " + command)
    command = input("Enter command: ")
else:
    print("Goodbye.")
print("Execution stopped.")