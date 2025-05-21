T = int(input())
V = int(input())
C = int(input())
M = int(input())

if V >= C + (M*2):
    result = (T * C * 2) + (T * M * 4)
elif C >= V + M:
    result = (T * V * 2) + (T * M * 2)
elif M >= (V*2) + C:
    result = (T * V * 4) + (T * C * 2)
else:
    result = (T * V * 2) + (T * M * 2)

print(result)