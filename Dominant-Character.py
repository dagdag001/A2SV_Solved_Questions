patterns = ["aa", "aba", "aca", "acba", "abca", "abbacca", "accabba"]

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    ans = float('inf')

    for p in patterns:
        if p in s:
            ans = min(ans, len(p))

    print(-1 if ans == float('inf') else ans)