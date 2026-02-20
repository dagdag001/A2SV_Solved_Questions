t = int(input())
for _ in range(t):
    n, x, k = map(int, input().split())
    s = input().strip()

    pos = x

    for i in range(n):
        if pos == 0:
            break
        if k == 0:
            break
        pos += -1 if s[i] == 'L' else 1
        k -= 1

    ans = 1 if pos == 0 and k >= 0 else 0

    cycle_pos = 0
    cycle_len = 0

    for ch in s:
        cycle_pos += -1 if ch == 'L' else 1
        cycle_len += 1
        if cycle_pos == 0:
            break

    if cycle_pos == 0 and pos == 0:
        ans += k // cycle_len

    print(ans)