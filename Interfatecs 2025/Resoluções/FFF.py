N = int(input())
elementos = []

for _ in range(N):
    elementos.append(int(input()))

maxNegativo = 0
total = 0

for suprimento in elementos:
    total += suprimento

    if total < 0 and total < maxNegativo:
        maxNegativo = total

result = abs(maxNegativo)

print(result)
