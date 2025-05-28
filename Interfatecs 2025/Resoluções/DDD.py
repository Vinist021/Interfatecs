n = int(input())
arr = list(map(int, input().split()))

somaMax = float('-inf')
    
for k in range(1, ((n//2) + 1)):
        
    for inicio in range(k):
        somaAtual = 0

        for i in range(inicio, n, k):
            somaAtual = max(somaAtual + arr[i], arr[i])
            somaMax = max(somaMax, somaAtual)
    
if somaMax == float('-inf'):
    somaMax = max(arr)
    
print(somaMax)