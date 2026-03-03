t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    casinos = []
    
    for _ in range(n):
        l, r, real = map(int, input().split())
        casinos.append((l, r, real))
    
    current = k
    
    while True:
        best = current
        for l, r, real in casinos:
            if l <= current <= r:
                if real > best:
                    best = real
        
        if best == current:
            break
        
        current = best
    
    print(current)