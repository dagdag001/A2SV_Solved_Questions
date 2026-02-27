from collections import Counter

T = int(input())
for _ in range(T):
    s = input().strip()
    t_str = input().strip()
    
    if Counter(s) - Counter(t_str):
        print("Impossible")
        continue
    
    extra = sorted((Counter(t_str) - Counter(s)).elements())
    
    c = s[0]
    less = [x for x in extra if x < c]
    equal = [x for x in extra if x == c]
    greater = [x for x in extra if x > c]
    
    option1 = "".join(less) + s + "".join(equal) + "".join(greater)
    option2 = "".join(less) + "".join(equal) + s + "".join(greater)
    
    print(min(option1, option2))