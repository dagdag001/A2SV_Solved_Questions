from collections import Counter
t = int(input())
for _ in range(t):
    s = input()
    t = input()
    cs = Counter(s)
    ct = Counter(t)
    for ch in cs:
        if ct[ch] < cs[ch]:
            print("IMPOSSIBLE")
            continue
        
    count = ct- cs
    res = []
    for char in count:
        for _ in range(count[char]):
            res.append(char)
    res.append(s)
    res.sort()
    print("".join(res))
