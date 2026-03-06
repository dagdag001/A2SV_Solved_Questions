t = int(input())

for _ in range(t):
    n = int(input())
    a = list(input().strip())
    b = list(input().strip())

    balance = [0]*n
    zero = one = 0

    for i in range(n):
        if a[i] == '0':
            zero += 1
        else:
            one += 1
        if zero == one:
            balance[i] = 1

    flip = 0
    possible = True

    for i in range(n-1, -1, -1):
        cur = a[i]
        if flip:
            cur = '1' if cur == '0' else '0'

        if cur != b[i]:
            if not balance[i]:
                possible = False
                break
            flip ^= 1

    print("YES" if possible else "NO")