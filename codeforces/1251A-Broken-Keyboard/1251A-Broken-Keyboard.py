t = int(input())

for _ in range(t):
    s = input().strip()
    working = set()
    
    i = 0
    n = len(s)
    
    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        
        if (j - i) % 2 == 1:
            working.add(s[i])
        
        i = j
    
    print("".join(sorted(working)))