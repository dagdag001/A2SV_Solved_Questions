t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    if k == 1:
        print(a[-1] - a[0])
        continue
    
    diffs = []
    for i in range(n - 1):
        diffs.append(a[i+1] - a[i])
    
    diffs.sort(reverse=True)
    
    total = a[-1] - a[0]
    subtract = sum(diffs[:k-1])
    
    print(total - subtract)