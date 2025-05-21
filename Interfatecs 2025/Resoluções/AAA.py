while True:
    entrada = input()
    nums = []

    if entrada == '*':
        print(0)
        break

    for i in entrada:
        if i == '*':
            nums.append(0)
        elif i == '.':
            nums.append(1)
        elif i == '-':
            nums.append(5)
        elif i == ' ':
            nums.append(' ')

    base = 0
    numTotal = 0
    nums = nums[::-1]

    for i in nums:
        if i == ' ':
            base += 1
            continue

        numTotal += i * (20 ** base)

    print(numTotal)