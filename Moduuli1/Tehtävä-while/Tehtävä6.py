import random
N = int(input("montako kertoja?:"))
n = kierrros = x =y = 0
while kierrros < N:
    kierrros += 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    print(f"x: {x}, y: {y}")
    kierrros += 1
    if x ** 2 + y ** 2 < 1:
        n += 1
print((4 * n / N))