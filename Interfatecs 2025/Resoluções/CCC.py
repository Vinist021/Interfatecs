N = int(input())

for _ in range(N):
    clima = input().split()
    T = float(clima[0])
    U = float(clima[1])
    P = int(clima[2])

    if P == 1:
        print('NAO REGAR')
    else:
        if T > 30.0 and U < 50.0:
            print('REGAR')
        else:
            print('NAO REGAR')