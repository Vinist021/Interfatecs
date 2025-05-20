Q = int(input())

for _ in range(Q):
    dorothy = int(input())
    dagmar = int(input())

    soma = dorothy + dagmar

    if dorothy > dagmar:
        if soma > 40:
            print('DOROTHY DECIDE E A NONNA VAI')
        else:
            print('DOROTHY DECIDE')

    elif dagmar > dorothy:
        if soma > 40:
            print('DAGMAR DECIDE E A NONNA VAI')
        else:
            print('DAGMAR DECIDE')