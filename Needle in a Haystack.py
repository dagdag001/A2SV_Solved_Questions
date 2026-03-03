from collections import Counter


T = int(input())
for _ in range(T):
    s = input().strip()
    t = input().strip()
    
    cs = Counter(s)
    ct = Counter(t)
    
    # Check if possible
    if cs - ct:
        print("Impossible")
        continue
    
    extra = ct - cs
    
    extra_sorted = sorted(extra.elements())
    
    c = s[0]
    
    less = []
    equal = []
    greater = []
    
    for ch in extra_sorted:
        if ch < c:
            less.append(ch)
        elif ch == c:
            equal.append(ch)
        else:
            greater.append(ch)
    
    option1 = "".join(less) + s + "".join(equal) + "".join(greater)
    option2 = "".join(less) + "".join(equal) + s + "".join(greater)
    
    print(min(option1, option2))
