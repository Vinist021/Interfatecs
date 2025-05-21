from math import sin

pi = 3.14159265358979323846

while True:
    entrada = input().split()
    a = float(entrada[0])
    b = float(entrada[1])
    theta = float(entrada[2])

    if a == 0 and b == 0 and theta == 0:
        break

    rad = (2 * pi * theta) / 360.0

    area = a * b * sin(rad) / 2

    print(f'{area:.4f}')